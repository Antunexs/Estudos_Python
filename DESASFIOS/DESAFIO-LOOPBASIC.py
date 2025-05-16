#Exercício 1
''' Loop Básico com FOR (Fácil)
Crie um programa que peça ao usuário um número inteiro N 
e imprima os números de 1 a N usando um loop FOR.
'''
numero = int(input("Insira um numero para uma contagem ate o mesmo: "))

for i in range(1 , numero + 1):
    print(i)


#Exercício 2
''' Soma de Ímpares (Médio)
Escreva um programa que peça ao usuário um número N 
e calcule a soma de todos os números ímpares de 1 a N utilizando um loop while.
'''
numero = int(input("Insira um numero: "))

soma = 0
num = 1


while num <= numero:
    if num % 2 != 0:
            soma += num
    num += 1
    
    print(f"A soma do numeros de 1 até {numero} é: {soma}")




#Exercício 3
''' Descobrindo Números Primos (Difícil)
Crie um programa que peça ao usuário um número N 
e exiba todos os números primos de 1 a N. 
Utilize loops aninhados para verificar se um número é primo.
'''
#Impossible kkkkk
     


#Exercício 4
''' Contagem regressiva com While (Fácil)
Peça ao usuário um número inteiro N 
e exiba uma contagem regressiva de N até 1 usando um loop while.
'''
numero = int(input("Insira um numero: "))
n = 0

while n < numero:
    n += 1
    print(n)
