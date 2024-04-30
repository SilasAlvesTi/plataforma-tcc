from django.contrib import admin
from .models import Turma, Questao, Aluno, Restultados


class TurmaAdmin(admin.ModelAdmin):
    pass

class QuestaoAdmin(admin.ModelAdmin):
    pass

class AlunoAdmin(admin.ModelAdmin):
    pass

class RestultadosAdmin(admin.ModelAdmin):
    pass


admin.site.register(Turma, TurmaAdmin)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Restultados, RestultadosAdmin)