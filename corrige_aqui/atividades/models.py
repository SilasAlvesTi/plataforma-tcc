from django.db import models
import jsonfield

class Questao(models.Model):
    enunciado = models.TextField()
    casos_de_teste = jsonfield.JSONField(default=dict)