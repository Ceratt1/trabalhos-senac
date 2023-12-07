import os
from classes import *
import json
users = {}
tasks = {}
menu = """
0 - mostrar todas tarefas e users
1 - Criar usuario
2 - criar tarefa
3 - atribuir tarefa a usuario
4 - exit"""

def criarTarefa(): #criar for para mostrar usuarios pela key do dict
    numero_pessoas_lista = len(users)
    if numero_pessoas_lista != 1:
        mostrarUsuarios()
        responsavel = input("digite o nome do responsável pela tarefa: ")
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
        
        
        
    else:
        print("necessitamos de usuarios ativos para atribuir tarefas!")
    
def criaruser():
    nome = input('digite seu nome: ')
    while True:
        email= input('digite seu email: ')
        if "@gmail.com" in email:
            break
        else:
            print("aceitamos apenas emails!")
    
    userobject = usuario(nome=nome, email=email)
    users[nome] = userobject.__dict__
    
def mostrarUsuarios():
    if len(users) != 0:
        for myusers in users.keys():
            print (myusers)




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




if __name__ == "__main__":
    script_name = os.path.basename(__file__)
    if script_name == "main.py":
        while True:
            print(menu)
            escolha = recebernumero()
            if escolha == 0:
                print("ok!\n\n")
            elif escolha == 1:
                criaruser()
            elif escolha == 2:
                criarTarefa()
            elif escolha == 3:
                pass
            elif escolha == 4:
                print("programa finalizado")
                break
            else:
                #nunca ira passar de 4, porém apenas por cuidado
                print("escolha algumas das opções abaixo")

    else:
        print("execute o arquivo 'main.py'")


