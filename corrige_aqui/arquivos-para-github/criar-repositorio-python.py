import os, subprocess, datetime
import shutil
import requests

repo_name = "primeiro-repositorio-" + str(datetime.datetime.now().strftime('%d-%m-%y-%H-%M-%S.%f'))
commit_message = "Primeiro commit"
branch_name = "main"

github_token = os.environ.get("TOKEN")

url = "https://api.github.com/user/repos"

data = {
    "name": repo_name,
    "private": False
}

headers = {
    "Authorization": f"Bearer {github_token}"
}

#response = requests.post(url, headers=headers, json=data)

script_name="./arquivos-para-github/tmp/create-repository.sh"
script_content = f"""#!/bin/bash

GITHUB_USERNAME="SilasTests"
REPO_NAME="{repo_name}"
TOKEN=$TOKEN


git init
git add .
git reset -- criar-repositorio-python.py create-repository.sh
git commit -m "Primeiro commit"

git remote add atividade https://$GITHUB_USERNAME:$TOKEN@github.com/$GITHUB_USERNAME/$REPO_NAME.git

git push -u atividade main"""

with open(script_name, 'w') as writer:
    writer.write(script_content)

os.chmod(script_name, 0o755)

#subprocess.call([f"./{script_name}"])

shutil.rmtree(".arquivos-para-github/tmp/")
os.mkdir(".arquivos-para-github/tmp")

""" if response.status_code == 201:
    print(f"Repositório '{repo_name}' criado com sucesso!")
else:
    print(f"Falha ao criar o repositório. Código de status: {response.status_code}")
    print(response.text) """