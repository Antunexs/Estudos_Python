# Exercício: Sistema de Presença na Sala de Aula
# Você foi encarregado de criar um pequeno sistema em Python que registra os alunos presentes em uma aula.


print("Presença na Sala de Aula")

alunos_sala = ["Davi", "matheus","Lucas", "Letycia", "Luana"]

presenca = {
    alunos_sala[0]: False,
    alunos_sala[1]: False,
    alunos_sala[2]: False,
    alunos_sala[3]: False,
    alunos_sala[4]: False
}

print(presenca)

aluno = 1

for aluno in alunos_sala:
    print(f"Aluno {alunos_sala[aluno]} está presente? (S/N): ")
