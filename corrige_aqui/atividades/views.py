from django.shortcuts import render, redirect
from django.conf import settings
from .models import Questao

import os, shutil, datetime, unicodedata

def index(response):
    return render(response, "atividades/index.html", {})

def criar_arquivo_de_testes(caso_de_teste):

    test_template = """
def test_case_{index}():
    input_data = "{input_data}"
    expected_result = "{expected_result}"
    cast_type = type(expected_result)

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,  
    )
    assert cast_type(result.stdout.decode()) == expected_result
    """

    test_code = ""
    for index, test_data in enumerate(caso_de_teste):
        input_data_tuple = test_data["input"]
        list_of_strings = [str(value) for value in input_data_tuple]
        input_data = "".join(list_of_strings)
        expected_result = test_data["expected_output"]
        test_code += test_template.format(index=index, input_data=input_data, expected_result=expected_result)

    
    with open("./arquivos-para-github/tmp/test_file.py", "w") as file:
        file.write("import subprocess\n\n")
        file.write(test_code)


def criar_readme(enunciado):
    with open("./arquivos-para-github/tmp/README.md", "w") as file:
        file.write(enunciado)


def criar_repositorio(linguagem, repositorio):
    path_linguagem = "./arquivos-para-github/" + linguagem
    path_temp = "./arquivos-para-github/tmp"
    path_create_repo = "./arquivos-para-github/criar-repositorio-python.py"
    
    shutil.copytree(path_linguagem, path_temp, dirs_exist_ok = True)
    shutil.copy(path_create_repo, path_temp + "/criar-repositorio-python.py")
    
    os.system("python ./arquivos-para-github/criar-repositorio-python.py " + repositorio)


def adicionar_atividade(request):
    if request.method == 'POST':
        repositorio = request.POST['repositorio']
        enunciado = request.POST['descricao']
        linguagem = request.POST['linguagem']

        titulos = (request.POST.getlist('titulo'))
        entradas = (request.POST.getlist('entrada'))
        saidas = (request.POST.getlist('saida'))
        casos_de_teste = []
        for i in range(0, len(titulos)):
            teste = {"titulo": titulos[i], "input": entradas[i], "expected_output": saidas[i]}
            casos_de_teste.append(teste)


        repo_name = repositorio.replace(" ", "-") + "-" + str(datetime.datetime.now().strftime('%d-%m-%y-%H-%M-%S.%f'))
        repo_name = unicodedata.normalize('NFKD', repo_name).encode('ASCII', 'ignore').decode('ASCII')

        Questao.objects.create(repo_name=repo_name, enunciado=enunciado, titulo="titulo", casos_de_teste=casos_de_teste)

        
        criar_arquivo_de_testes(caso_de_teste=casos_de_teste)
        criar_readme(enunciado)
        criar_repositorio(linguagem, repo_name)

        return redirect(settings.BASE_URL + 'atividades/') 
    return render(request, 'index.html')