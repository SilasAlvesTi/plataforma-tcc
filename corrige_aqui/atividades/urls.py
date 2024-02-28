from django.urls import path

from . import views

app_name = "atividades"
urlpatterns = [
    path("", views.index, name="index"),
    path("adicionar/", views.adicionar_atividade, name="adicionar-atividade")
]
