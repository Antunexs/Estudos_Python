print("Calculadora IMC")
print()

nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

altura = float(input("Digite sua altura: "))

peso = float(input("Digite seu peso: "))
print()

print(f"Seu nome é {nome}\nSua altura é {altura}\nSeu peso é {peso}")

imc = peso / (altura * altura)
print()
print(f"Seu IMC é : {imc:.2f}" )
 
#Tabela IMC
print()
if imc < 18.5 :
    print("Sua Classificação Magreza")
elif imc < 24.9 :
    print("Sua Classificação Normal")   
elif imc < 29.9 :
    print("Sua Classificação Sobrepeso") 
elif imc < 34.9 :
    print("Sua Classificação Obesidade grau I") 
elif imc < 39 :
    print("Sua Classificação Obesidade grau I") 
elif imc > 40 :
    print("Sua Classificação Obesidade grau III")  

