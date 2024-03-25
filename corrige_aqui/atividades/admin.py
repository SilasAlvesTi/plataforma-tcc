from django.contrib import admin
from .models import Turma, Questao, Aluno


class TurmaAdmin(admin.ModelAdmin):
    pass

class QuestaoAdmin(admin.ModelAdmin):
    pass

class AlunoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Turma, TurmaAdmin)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Aluno, AlunoAdmin)