import os 

os.system('cls')


class user():
    def __init__(self, nome, email, task) -> None:
        self.nome = nome
        self.email = email
        self.task = task
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

    def __str__(self) -> str:
        return f"Nome: {self.titulo} Descricao: {self.desc} Status:{self.status}"


t1 = task("jogar", "codar")

u1 = user("gabriel", "x1@gmail.com", t1 )


print (u1)




