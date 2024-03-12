from django.urls import path

from . import views

app_name = "plataforma"
urlpatterns = [
    path("", views.index, name="index"),
    path("usuario/", views.redirecionar_usuario, name="redirecionar-usuario")
]
