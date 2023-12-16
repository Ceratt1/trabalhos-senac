import os 

os.system('cls')

tarefas_dict = {}
users_dict = {}



class user():
    def __init__(self, nome, email) -> None:
        self.nome = nome
        self.email = email
        self.task = None
    
    def coletarTask(self):
        if self.task == None:
            while True:
                print (list(tarefas_dict))
                selectTask = input("Digite o nome da sua task: ")
                if selectTask in list(tarefas_dict):
                    print ("tarefa atribuida!")
                    self.task = tarefas_dict[selectTask]
                    break
                else:
                    print("tarefa não localizada")
        else:
            print("Opa! você ja está com uma task ativa, finalize está primeiro!")
 
    def altdesc(self):
        if self.task != None:
            self.task.alterarDesc()
        else:
            print("você precisa ter uma task primeiro!")

    def finalizarTask (self):
        if self.task != None:
            self.task.excluirTask()
            self.task = None
        else:
            print ("Você não tem tasks ativas")



    def __str__(self) -> str:
        return f"Nome: {self.nome}\nEmail: {self.email}\nTasks:{self.task}"


class task ():
    def __init__(self, titulo, desc, status = True) -> None:
        self.titulo = titulo
        self.desc = desc
        self.status = status
    
    def alterarDesc(self):
        while True:
            testDesc = input("Digite sua nova descrição:\n")
            if len(testDesc) > 120:
                print ("digite uma descrição menor!")
            else:
                self.desc = testDesc
                break
    def excluirTask(self):
        if self.titulo in list(tarefas_dict):
            del tarefas_dict[self.titulo]
            print ("tarefa excluida!")

        else:
            print("Tarefa não localizada!")



    def __str__(self) -> str:
        return f"Nome: {self.titulo} Descricao: {self.desc} Status:{self.status}"


# t1 = task("jogar", "codar")
# u1 = user("gabriel", "x1@gmail.com")
# tarefas_dict[t1.titulo] = t1
# print (tarefas_dict)

# u1.coletarTask()
# print (u1)

# u1.altdesc()
# print (u1)










# u1.finalizarTask()
# print(u1)
# print(tarefas_dict)
# u1.finalizarTask()
# print(u1)