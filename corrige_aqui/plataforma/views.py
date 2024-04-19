from django.shortcuts import redirect, render

from django.conf import settings

def index(request):
    print('index')
    return render(request, "plataforma/index.html", {})

def redirecionar_usuario(request):
    if request.method == 'POST':
        if request.POST['usuario'] == "aluno":
            return redirect(settings.BASE_URL + 'atividades/aluno/') 
        return redirect(settings.BASE_URL + 'atividades/') 