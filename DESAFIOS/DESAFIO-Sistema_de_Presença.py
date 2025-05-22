# Exercício: Sistema de Presença na Sala de Aula
# Você foi encarregado de criar um pequeno sistema em Python que registra os alunos presentes em uma aula.


print(f"Presença na Sala de Aula\n")

alunos_sala = ["Davi", "Matheus","Lucas", "Letycia", "Luana"]

presentes = []

ausentes = []

presenca = {
    alunos_sala[0]: False,
    alunos_sala[1]: False,
    alunos_sala[2]: False,
    alunos_sala[3]: False,
    alunos_sala[4]: False
}

print(f"Alunos na turma: ", alunos_sala)
print()

x = 0

while x < len(alunos_sala):
    pres = input(f"Aluno {alunos_sala[x]} está presente? (S/N): ").strip().upper()
    
    if pres == "S":
        presenca [alunos_sala[x]] = True
        presentes.append(alunos_sala[x]) 
        x += 1
        
    else :
        presenca [alunos_sala[x]] = False
        ausentes.append(alunos_sala[x]) 
        x += 1
        
print()    
print(f"Presentes ({len(presentes)}): {presentes}")
print(f"Ausentes ({len(ausentes)}): {ausentes}")







