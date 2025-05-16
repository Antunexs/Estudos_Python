# LISTAS
# int[] list = new int [];

#                0  1  2  3  4
#               -5 -4 -3 -2 -1
lista_numeros = [1, 2, 3, 4, 5]
# print(type(lista_numeros))
# print(listaNumeros)
# print(len(listaNumeros))

# lista_nova = [10, 9, 8, 7, 6] # for


coordenada = '1,2'

lista = [1, 'string', 3.4556, 1, 1]

# acessando um índice da lista
print(lista[0])

# Manipulação de listas
lista.append(coordenada) #Adiciona um Valor ao final da lista 
print(lista)

lista.pop() # Remove um valor de acordo com o indice, se não passar o indice ele remove o ultimo

print(lista)

print(lista.count(1))# Conta ocorrências de um determinado valor dentro de uma lista 

# print(lista.sort()) # valores do mesmo tipo

print(lista.index('string')) # procura o indice, onde ocorre o primeiro valor 

lista.insert(2, 'olá') #substituir valor passando o (indice, valor)
print(lista)

lista[-1] = 100
print(lista)


# LISTAS SÃO ITERÁVEIS - pode ser pecorrida
# i = 0
# while i < len(lista_numeros):
#     print(lista_numeros[i])
#     i+=1


# for indice in lista_nova:
#     print(indice)

# LISTA DE LISTAS
lista = [
    ['nome', 'antunes'],
    ['idade', 24]
]

print(lista[1][1])


## Desafio 
'''
utilizando listas, crie uma simulação de fila de caixa de supermecardo 

'''