import os
from classes import *
import json
users = []
tasks = []



def criarTarefa(self):
    nome = self.nome
    titulo = input("digite o titulo da sua tarefa: ")
    descricao = input("digite a descricao da sua tarefa: ")
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
    
    

















# if __name__ == "__main__":
#     script_name = os.path.basename(__file__)
#     if script_name == "main.py":
#         print("hii")






# arquivo abaixo de test

# if __name__ == "__main__":
#     script_name = os.path.basename(__file__)
#     if script_name == "main.py":
#         pass
#     else:
#         print("execute o arquivo 'main.py'")


