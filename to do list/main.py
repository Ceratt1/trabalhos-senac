import os
from classes import *
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
    print(menu_semtaskativa)
    











while True:
    print (menu_um)
    resposta = returns()
    
    if resposta == 1:
        print("programa finalizado!")
        break
    elif resposta == 2:
        criarConta()
    elif resposta == 3:
        nameLogin = login()
        if nameLogin != None:
            nameUser = users_dict[nameLogin]
            if nameUser.task != None:
                print("Menu caso tenha task ativa")
            else:
                semtask()
    

    else:
        print("aceitamos apenas números entre as respostas")