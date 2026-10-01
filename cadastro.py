alunos = []

def adicionar():
    nome = input("qual o nome do aluno?    ")
    idade = int(input("qual a idade do aluno?   "))
    nota = float(input("qual a nota do aluno?     "))

    while nota < 0 or nota >10:
        nota = float(input("insira um valor entre 0 e 10"))

    alunos.append({"nome": nome, "idade": idade, "nota": nota})

def listar():
     if not alunos:
        print(" aluno não cadastrado.")
     else:
        for aluno in alunos:
            print(aluno)

def buscar():
    nome = input("qual o nome do aluno?  ")

    for aluno in alunos:
        if aluno["nome"] == nome:
            print(aluno)
            return
    print("aluno não cadastrado.")

def remover():
    nome = input("qual o nome do aluno?  ")

    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("aluno Removido.")
            return
    print("aluno não cadastrado.")

def media():
    if alunos:
       total = 0
       for aluno in alunos:
           total= total + aluno["nota"]
       resultado = total/len(alunos)
       print(" Media", resultado)

    else:
        print("aluno não cadastrado.")

while True:
    print("1 - adicionar   2 - Listar   3 - Buscar   4 - Remover   5 - Media    6 - Sair")
    op = input("Opção:  ")

    if op == "1":
        adicionar()

    elif op == "2":
        listar()

    elif op == "3":
        buscar()

    elif op == "4":
       remover()

    elif op == "5":
        media()

    elif op == "6":
        break

    else:
        print("Opção invalida.")
