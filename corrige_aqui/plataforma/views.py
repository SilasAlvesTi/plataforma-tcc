from django.shortcuts import redirect, render
from atividades.models import Turma, Professor, AlunoTurma, Aluno

from django.conf import settings

def index(request):
    return render(request, "plataforma/index.html", {})

def redirecionar_usuario(request):
    if request.POST['usuario'] == "aluno":
        return escolher_turma(request, "aluno")
    return escolher_turma(request, "professor")
    

def escolher_turma(request, usuario):
    if usuario == "professor":
        professor = Professor.objects.last()
        turmas = Turma.objects.filter(professor_id=professor.id)
        return render(request, "plataforma/turmas.html", {"turmas": turmas, "professor": professor})
    
    if usuario == "aluno":  
        aluno = Aluno.objects.last()
        alunoTurma = AlunoTurma.objects.filter(aluno_id=aluno.id)
        if alunoTurma:
            turmas = []
            for turma in alunoTurma:
                if Turma.objects.filter(id=turma.turma_id).exists():
                    turmas.append(Turma.objects.get(id=turma.turma_id)) 
            return render(request, "plataforma/turmas.html", {"turmas": turmas, "aluno": aluno})
    turmas = Turma.objects.all()
    return render(request, "plataforma/matricular.html", {"turmas": turmas, "aluno": aluno})


def matricular_aluno(request):
    turma_id = request.POST.get("turma")
    aluno_id = request.POST.get("aluno")
    turma = Turma.objects.get(id=turma_id)
    aluno = Aluno.objects.get(id=aluno_id)
    AlunoTurma.objects.create(turma=turma, aluno=aluno)

    return render(request, "plataforma/index.html", {})

def adicionar_turma(request):
    nome = request.POST['turma'] 
    professor = Professor.objects.last()
    turma = Turma.objects.create(nome=nome, professor=professor)
    turmas = Turma.objects.all()
    return render(request, "plataforma/turmas.html", {"turmas": turmas, "professor": professor, "turma": turma})
