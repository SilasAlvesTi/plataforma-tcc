from django.urls import path

from . import views

app_name = "atividades"
urlpatterns = [
    path("", views.index, name="index"),
    path("adicionar/", views.adicionar_atividade, name="adicionar-atividade"),
    path("aluno/", views.mostrar_repositorios, name="mostrar-repositorios"),
    path("aluno/adicionar/", views.adicionar_repositorio, name="adicionar-repositorio")
]
