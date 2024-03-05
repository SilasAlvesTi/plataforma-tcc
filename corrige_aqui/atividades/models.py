from django.db import models
import jsonfield

class Questao(models.Model):
    repo_name = models.CharField(max_length=50)
    enunciado = models.TextField()
    casos_de_teste = jsonfield.JSONField(default=dict)