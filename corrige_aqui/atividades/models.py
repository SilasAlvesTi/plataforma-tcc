from django.db import models
import jsonfield


class Professor(models.Model):
    nome = models.CharField(max_length=50)


class Turma(models.Model):
    nome = models.CharField(max_length=50, default='turma')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)


class Questao(models.Model):
    repo_name = models.CharField(max_length=50)
    enunciado = models.TextField()
    titulo = models.TextField()
    casos_de_teste = jsonfield.JSONField(default=dict)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)


class Aluno(models.Model):
    nome = models.CharField(max_length=50, default="aluno teste")

class AlunoQuestao(models.Model):
    repo_name = models.CharField(max_length=50)
    nota = models.IntegerField()
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)


class AlunoTurma(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    