# Generated by Django 5.0.2 on 2024-04-08 17:40

import django.db.models.deletion
import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_name', models.CharField(max_length=50)),
                ('nota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='turma', max_length=7)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividades.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_name', models.CharField(max_length=50)),
                ('enunciado', models.TextField()),
                ('titulo', models.TextField()),
                ('casos_de_teste', jsonfield.fields.JSONField(default=dict)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividades.turma')),
            ],
        ),
        migrations.CreateModel(
            name='AlunoTurma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividades.aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividades.turma')),
            ],
        ),
    ]
