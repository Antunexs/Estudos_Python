# Loop
# While / For

# for (i = 0, i < n, i++) {
    
# }

indiceIncial = 0
maximo = 10
# step = 3
while indiceIncial < maximo:
    print(indiceIncial)
    indiceIncial += 1
    if indiceIncial == 6:
        break

# Loop FOR
for i in range(indiceIncial, maximo):
    print(f"printando {i}")


while True:
    variavel = input("Digite uma mensagem e clique enter: ") # ele retornará uam string
    
    if variavel == 'sair':
        print('até logo...')
        break

    print(f'Variável é {variavel}')