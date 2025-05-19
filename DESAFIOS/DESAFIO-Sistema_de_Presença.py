# Exercício: Sistema de Presença na Sala de Aula
# Você foi encarregado de criar um pequeno sistema em Python que registra os alunos presentes em uma aula.


print("Presença na Sala de Aula")

alunos_sala = ["Davi", "Matheus","Lucas", "Letycia", "Luana"]

presenca = {
    alunos_sala[0]: False,
    alunos_sala[1]: False,
    alunos_sala[2]: False,
    alunos_sala[3]: False,
    alunos_sala[4]: False
}

print(presenca, f"\n ")

i = True
x = 0

# print (len(presenca))

while i == True:
    pres = input(f"Aluno {alunos_sala[x]} está presente? (S/N): ").strip().upper()
    
    if pres == "S":
        presenca [alunos_sala[x]] = True
        x += 1
        
    else :
        presenca [alunos_sala[x]] = False
        x += 1
    
    if x == (len(presenca) - 1):
        # break
        i = False    
    
# print(len(alunos_sala))









