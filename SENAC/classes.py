import os;
import json
from datetime import datetime
data_atual = datetime.now().date()
os.system('cls')

class usuario:
    def __init__(self, nome,email):
        self.nome = nome
        self.email = email
        self.tarefas = []

class tarefa:
    def __init__(self, responsavel ,tituloTarefa, descTarefa, data, sttsTarefa = False):
        self.responsavel = responsavel
        self.titulo = tituloTarefa
        self.descricao = descTarefa
        self.status = sttsTarefa
        self.data = data
    def alterarStatus(self):
        if self.status == False:
            self.status = True
    def attDesc (self):
        novaDescricao = input("digite sua nova descrição: ")
        self.descricao = novaDescricao
        print("descrição atualizada")
    def finalizarTarefa (self):
        pass
    def __str__(self) -> str:
        return f"Responsável : {self.responsavel} | Nome: {self.titulo} | Descricao = {self.descricao} | status: {self.status} | Data: {self.data}"
    


a = tarefa("Rafa", "chupar um pau", "grande e grosso", data_atual)


print (a)