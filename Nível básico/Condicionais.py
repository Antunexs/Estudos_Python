# if (){
  
#  } else {
     
#  }}#

#Condicionas 
# IF ELIF ELSE

numero1 = 20
numero2 = 50

if numero1 < numero2 :
    print(f" {numero1} é menor que {numero2}")
elif numero1 > numero2:
    print(f"{numero1} não é maior que {numero2}")
else : 
    print("ERRO")

# MatchCase disponível a partir do 3.10

portal = 0

match portal :
    case True :
        print("portal está aberto")
    case False :
        print("O portão está fechado")
    case _:
        print("Erro de valor")

# boolean variavel = True
# if True:
#     ...