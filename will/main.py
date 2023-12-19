import os
from classes import *
import json


menu_um = """
1 - sair
2 - criar user
3 - login
"""

menu_semtaskativa = """
1 - exit
2 - Criar task
3 - Coletar Task
4 - Mostrar tasks pendentes
"""

menu_task_ativa ="""
1 - exit
2 - Finalizar task
3 - Alterar descrição
4 - Mostrar tasks pendentes
"""

def returns():
    while True:
        try:
            resposta = int(input("Digite a resposta: "))
            if resposta in [1,2,3, 4]:
                return resposta
                break
            else:
                print("aceitamos apenas números entre as respostas")
            
        except:
            print("Aceitamos apenas números!")

def criarConta():
    nome = input("digite o nome: ")
    while True: #gerar email
        email = input('digite seu email: ')
        if "@gmail.com" in email:
            break
        else:
            print("aceitamos apenas emails!")
    criarUser = user(nome=nome, email= email)
    users_dict[nome] = criarUser
    print ("\nconta criada!")

def login():
    if len(list(users_dict.keys())) != 0:
        print (list(users_dict.keys()))
        while True:
            nome = input("Digite o nome que deseja logar: ")
            if nome in list(users_dict.keys()):
                print("\nconta logada\n")
                return nome
                break
            else:
                print("Conta não encontrada!")
    else:
        print("\nNecessário ter uma conta!\n")

def semtask():
    while True:
        print(menu_semtaskativa)
        segundo_menu = returns()
        if segundo_menu == 1:
            print("deslogando...")
            return True
            break
        if segundo_menu == 2:
            titulo = input("digite o titulo da sua task: ")
            Descricao = input("digite a descrição da sua task:")
            newTask = task(titulo=titulo, desc=Descricao)
            tarefas_dict[titulo] = newTask
            print ("\n\n\ntarefa gerada com sucesso!\n\n\n")
        if segundo_menu == 3:
            if len(list(tarefas_dict.keys())) != 0:
                nameUser.coletarTask()
                break
            else:
                print("é necessário criar uma tarefa primeiro!")
        if segundo_menu == 4:
            print(f"Temos um total de {len(list(tarefas_dict.keys()))} pendentes, sendo ela/as:\n{list(tarefas_dict.keys())}")
        else:
            pass
    
def comtask():
    while True:
        print(menu_task_ativa)
        terceiroMenu = returns()
        if terceiroMenu == 1:
            print("deslogando . . .")
            break
        elif terceiroMenu == 2:
            nameUser.finalizarTask()
            
        elif terceiroMenu == 3:
            print(f"Task Atual: {nameUser.task}")
            nameUser.altdesc()
            print(f"Task atualizada: {nameUser.task}")


        elif terceiroMenu == 4:
            print(f"Temos um total de {len(list(tarefas_dict.keys()))} pendentes, sendo ela/as:\n{list(tarefas_dict.keys())}")
        else:
            print("aceitamos apenas números entre as respostas")



while True:
    print (menu_um)
    resposta = returns()
    
    if resposta == 1:
        print("\nprograma finalizado!!!!!!!")
        break
    elif resposta == 2:
        criarConta()
    elif resposta == 3:
        nameLogin = login()
        while True:
            if nameLogin != None:
                nameUser = users_dict[nameLogin]
                if nameUser.task != None:
                    comtask()
                else:
                    saida = semtask()
                    if saida == True:
                        break
                    

    else:
        print("aceitamos apenas números entre as respostas")