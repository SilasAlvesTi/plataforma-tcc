from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include("plataforma.urls")),
    path('atividades/', include("atividades.urls")),
    path('admin/', admin.site.urls),
]