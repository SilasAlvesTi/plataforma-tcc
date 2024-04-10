from django.urls import path

from . import views

app_name = "plataforma"
urlpatterns = [
    path("", views.index, name="index"),
    path("usuario/", views.redirecionar_usuario, name="redirecionar-usuario"),
    path("turmas/", views.escolher_turma,  name="escolher-turma"),
    path("turmas/adicionar", views.adicionar_turma,  name="adicionar-turma"),
    path("turmas/matricular", views.matricular_aluno,  name="matricular-aluno"),
]
