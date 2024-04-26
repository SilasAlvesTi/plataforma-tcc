from django.urls import path

from . import views

app_name = "atividades"
urlpatterns = [
    path("", views.index, name="index"),
    path("adicionar-ou-listar/", views.adicionar_ou_listar_atividade, name="adicionar-ou-listar"),
    path("listar-alunos-do-repositorio/", views.listar_alunos_do_repositorio, name="listar-alunos-do-repositorio"),
    path("logs-aluno", views.logs_aluno, name="logs-aluno"),
    path("adicionar/", views.adicionar_atividade, name="adicionar-atividade"),
    path("aluno/", views.mostrar_repositorios, name="mostrar-repositorios"),
    path("aluno/adicionar/", views.adicionar_repositorio, name="adicionar-repositorio"),
    path("aluno/resultado/", views.pegar_resultados, name="pegar-resultados"),
]
