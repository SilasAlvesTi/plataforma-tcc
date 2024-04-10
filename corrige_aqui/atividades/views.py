from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Aluno, AlunoTurma, Questao, Turma

import os, shutil, datetime, unicodedata, re, base64
import xml.etree.ElementTree as ET
import requests

def index(request):
    turma_id = request.POST.get("turma")
    return render(request, "atividades/index.html", {"turma": turma_id[0]})

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
            teste = {"titulo": titulos[i], "input": entradas[i], "expected_output": saidas[i], "nome_no_arquivo_de_teste": f"test_case_{i}"}
            casos_de_teste.append(teste)


        repo_name = repositorio.replace(" ", "-") + "-" + str(datetime.datetime.now().strftime('%d-%m-%y-%H-%M-%S.%f'))
        repo_name = unicodedata.normalize('NFKD', repo_name).encode('ASCII', 'ignore').decode('ASCII')

        turma = Turma.objects.get(id=request.POST['turma'])
        print(turma.nome)
        #Questao.objects.create(repo_name=repo_name, enunciado=enunciado, titulo="titulo", casos_de_teste=casos_de_teste, turma=turma)

        """ criar_arquivo_de_testes(caso_de_teste=casos_de_teste)
        criar_readme(enunciado)
        criar_repositorio(linguagem, repo_name) """

        return redirect(settings.BASE_URL + 'atividades/') 
    return render(request, 'index.html')

def mostrar_repositorios(request):
    repositorios = Questao.objects.all()
    aluno = Aluno.objects.last()
    #nota = mostrar_resultados_aluno(aluno=aluno)
    """ context = {
        "repositorios": repositorios,
        "repo_aluno": aluno.repo_name,
        "nota": nota,
    } """

    context = {
        "repositorios": repositorios,
    }
    return render(request, "atividades/listagem-repositorios.html", context=context)

def mostrar_resultados_aluno(aluno):
    return aluno.nota

def adicionar_repositorio(request):
    aluno = Aluno.objects.create(repo_name=request.POST['repositorio'], nota=0)
    turma = Turma.objects.last()
    AlunoTurma.objects.create(turma=turma, aluno=aluno)
    context = {"repo_aluno": aluno.repo_name}
    return redirect(settings.BASE_URL + 'atividades/aluno/', context) 


def pegar_resultados(request):
    aluno = Aluno.objects.last()
    repo_name = aluno.repo_name
    repo_name = repo_name.split("github.com/", 1)[1]

    response = requests.get(
        f"https://api.github.com/repos/{repo_name}/contents/results.xml",
    )


    if response.status_code == 200:
        data = response.json()
        file_content = data['content']

        file_content_encoding = data.get('encoding')
        if file_content_encoding == 'base64':
            file_content = base64.b64decode(file_content).decode()

        padrao_falhas = r'failures=\"([^\"]*)\"'
        padrao_testes = r'tests=\"([^\"]*)\"'
        correspondencias_falhas = re.search(padrao_falhas, file_content)
        correspondencias_testes = re.search(padrao_testes, file_content)

        if correspondencias_falhas:
            total_falhas = correspondencias_falhas.group(1)

        if correspondencias_testes:
            total_testes = correspondencias_testes.group(1)
        print(f"total falhas {total_falhas}, total testes {total_testes}")
        testes_corretos = int(total_testes) - int(total_falhas)
        resultado = (testes_corretos / int(total_testes)) * 100

        # Ler xml e pegar resultados
        tree = ET.fromstring(file_content)
        testsuite = tree.find("testsuite")

        for testcase in testsuite.findall("testcase"):
            if testcase.find("failure") is not None:
                nome_caso = testcase.get("name")
                resultado_esperado = testcase.find("failure").get("message").split("==")[1].strip()
                resultado_esperado = resultado_esperado.split("\n")[0]
                resultado_esperado = resultado_esperado.replace("'", "")
                valor_passado = testcase.find("failure").get("message").split("==")[0].strip()
                valor_passado = valor_passado.split("assert ")[1]
                valor_passado = valor_passado.replace("'", "")
                
                print(f"Nome do caso: {nome_caso}")
                print(f"Resultado esperado: {resultado_esperado}")
                print(f"Valor passado: {valor_passado}")
                print("-" * 40)

        """ aluno.nota = resultado
        aluno.save() """
    else:
        print(f"Error: {response.status_code}")

    context = {"repo_aluno": repo_name}
    return redirect(settings.BASE_URL + 'atividades/aluno/') 

  