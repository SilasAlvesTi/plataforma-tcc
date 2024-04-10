from django.contrib import admin
from .models import Turma, Questao, Aluno, Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',) 
    fields = ('nome',)

    
@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    pass


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass
