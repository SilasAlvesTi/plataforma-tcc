from django.db import models
import jsonfield


class Turma(models.Model):
    nome = models.CharField(max_length=7, default='turma', editable=False)


class Questao(models.Model):
    repo_name = models.CharField(max_length=50)
    enunciado = models.TextField()
    titulo = models.TextField()
    casos_de_teste = jsonfield.JSONField(default=dict)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)


class Aluno(models.Model):
    repo_name = models.CharField(max_length=50)
    nota = models.IntegerField()


class AlunoTurma(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)