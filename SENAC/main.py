import os
from classes import *
import json
users = {}
tasks = {}
menu = """
0 - mostrar todas tarefas
1 - Criar usuario
2 - criar tarefa
3 - atribuir tarefa a usuario
4 - exit"""

def criarTarefa():
    numero_pessoas_lista = len(users)
    print (numero_pessoas_lista)


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
    
def criaruser():
    nome = input('digite seu nome: ')
    while True:
        email= input('digite seu email: ')
        if "@gmail.com" in email:
            break
        else:
            print("aceitamos apenas emails!")
    
    



def recebernumero():
    numeros = [0,1,2,3,4]
    while True:

        try:
            escolha = int(input("digite sua escolha de acordo com o número: "))
            if escolha in numeros:
                return escolha
                break
            else:
                print ("Aceitamos apenas números dentro do limite das escolhas")
        except:
            print("Aceitamos apenas números de acordo com as opções do menu")

criaruser()





if __name__ == "__main__":
    script_name = os.path.basename(__file__)
    if script_name == "main.py":
        print(menu)
        escolha = recebernumero()
        if escolha == 1:
            pass
        elif escolha == 2:
            criarTarefa()
        elif escolha == 3:
            pass
        elif escolha == 4:
            print("programa finalizado")
        else:
            pass
    else:
        print("execute o arquivo 'main.py'")


