# import time
import os 
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal antes

print("Lançamento do foguete STAR_ESD_01 iniciando (Contagem regressiva\n")

contagemRegresiva = 10

for i in range (contagemRegresiva, 0 , -1):
    print(i)
    sleep(1.5) # Faz a contagem regressiva com intervalo de (1.5s)
    
    if i == 4 :
        print("Atenção")
    elif i == 1 :
        print("Lançamento do foguete !!!")

