from django.contrib import admin
from django.urls import include, path

app_name = "atividades"
urlpatterns = [
    path('atividades/', include("atividades.urls")),
    path('admin/', admin.site.urls),
]