


print("Sistema de Cadastro de Alunos e Notas")

nome_alunos = ["Maria", "João", "Miguel"]

lista_alunos = []

aluno_nota = {"nome" : None, "notas" : []}

notasBimestrais = []

alunos = len(nome_alunos)

while True:

    print(f"Professor adicione nota dos 4 bimestres \n")
        
    aluno_nota["nome"] = input("Insira o nome do aluno: ")
    nota1 = input(f"Insira a nota do primeiro bimestre do aluno {nome_alunos[0]} : ")
    nota2 = input(f"Insira a nota do segundo bimestre do aluno {nome_alunos[0]} : ")
    nota3 = input(f"Insira a nota do terceiro bimestre do aluno {nome_alunos[0]} : ")
    nota4 = input(f"Insira a nota do quarto bimestre do aluno {nome_alunos[0]} : ")

    notasBimestrais.extend([nota1 ,nota2 ,nota3 ,nota4])

    aluno_nota["notas"] = notasBimestrais

    print(aluno_nota)
    
    resposta = input()
    
    alunos += 1
    
    break