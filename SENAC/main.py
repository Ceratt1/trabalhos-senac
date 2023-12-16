import os
from classes import *
import json

users = {}
tasks = {}

menu = """
0 - mostrar todas tarefas e users
1 - Criar usuario
2 - criar tarefa
3 - exit"""

def criarTarefa():
    global users, tasks
    numero_pessoas_lista = len(users)
    if numero_pessoas_lista != 0:
        mostrarUsuarios()
        responsavel = responsavelverificar()
        titulo = input("digite o titulo da sua tarefa: ")
        descricao = input("digite a descricao da sua tarefa: ")
        date_time = data_atual 
        while True:
            status = input("Deseja ativar sua tarefa? S/N: ").upper()
            if status == "S":
                status = True
                break
            elif status == "N":
                status = False
                break
            else:
                print("Digite apenas S/N - - - - - - ")
        taskLocal = tarefa(responsavel=responsavel, tituloTarefa=titulo, descTarefa=descricao, data=data_atual)
        tasks[titulo] = taskLocal.__dict__
        users[responsavel]['tarefas'][titulo] = taskLocal.__dict__
        print(users[responsavel])        
    else:
        print("necessitamos de usuarios ativos para atribuir tarefas!")

def criaruser():
    global users
    nome = input('digite seu nome: ')
    while True:
        email = input('digite seu email: ')
        if "@gmail.com" in email:
            break
        else:
            print("aceitamos apenas emails!")

    userobject = usuario(nome=nome, email=email)
    users[nome] = {'info': userobject.__dict__, 'tarefas': {}}

def mostrarUsuarios():
    global users
    if len(users) != 0:
        print("usuarios ativos: ")
        for myusers in users.keys():
            print(f"-{myusers}")

def responsavelverificar():
    global users
    while True:
        responsavel = input("digite o nome do responsável pela tarefa: ")
        for x in users.keys():
            if responsavel == x:
                if len(users[responsavel]['tarefas']) == 0:
                    return responsavel
                else:
                    print(f"O user {responsavel} está ocupado com a tarefa {users[responsavel]['tarefas']} ")
            else:
                pass

def recebernumero():
    numeros = [0, 1, 2, 3]
    while True:
        try:
            escolha = int(input("digite sua escolha de acordo com o número: "))
            if escolha in numeros:
                return escolha
            else:
                print("Aceitamos apenas números dentro do limite das escolhas")
        except:
            print("Aceitamos apenas números de acordo com as opções do menu")

def mostrartasksandusers():
    global users, tasks
    if len(users) != 0:
        print("\nUsers Ativos:")
        for user in users.keys():
            print(f">{user}")
    else:
        print("não há users ativados")
    if len(tasks) != 0:
        print("\nTasks Ativas:")
        for task in tasks.keys():
            print(f">{task}")
    else:
        print("não há tasks ativas")

def iniciarPrograma():
    global users, tasks
    try:
        with open("users.json", "r") as usersjson2:
            users_lidos = json.load(usersjson2)
            users = users_lidos
        with open("tasks.json", "r") as tasksjson2:
            tasks_lidas = json.load(tasksjson2)
            tasks = tasks_lidas
    except:
        print("programa iniciado do zero!\n\n")

def finalizarPorgrama():
    global users, tasks
    try:
        with open("users.json", "r") as usersjson:
            users_lidos = json.load(usersjson)
            users = users_lidos
            print(users)
        with open("tasks.json", "r") as tasksjson:
            tasks_lidas = json.load(tasksjson)
            tasks = tasks_lidas
            print(tasks)
    except:
        with open("users.json", "w") as usersjson1:
            json.dump(users, usersjson1)
        with open("tasks.json", "w") as tasksjson1:
            json.dump(tasks, tasksjson1)

if __name__ == "__main__":
    script_name = os.path.basename(__file__)
    if script_name == "main.py":
        iniciarPrograma()
        while True:
            print(menu)
            escolha = recebernumero()
            if escolha == 0:
                print("ok!\n")
                mostrartasksandusers()
            elif escolha == 1:
                criaruser()
            elif escolha == 2:
                criarTarefa()
            elif escolha == 3:
                print("programa finalizado")
                finalizarPorgrama()
                break
            else:
                print("escolha algumas das opções abaixo")
    else:
        print("execute o arquivo 'main.py'")
