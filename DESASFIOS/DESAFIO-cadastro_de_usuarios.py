# Cadastro de usuarios
'''
Crie um sistema simples de cadastro de usuários utilzando dicionários dentro de uma lista.
Voce deve inserir os seguintes dados
- id
- Nome
- idade
- e-mail

O id deve ser gerado automaticamente quando o cadastro for conluido com sucesso
'''


print("Cadastro de usuário\n")

usuarios = []

repeticao = True

while repeticao :
    resposta = input("Deseja cadastrar um usuário ?(S / N)")
    
    if resposta == 'S':

        usuario = {
            "ID": None,
            "Nome": input("Nome: "),
            "Idade": input("Idade: "),
            "Email": input("Email: "),
        }
        
        if usuarios == []:
            print('Registrando novo usuário...')
            usuario['ID'] = 1
        else:
            print('consultando lista...') 
            print(usuarios[-1]['ID'])
            usuario["ID"] =  usuarios[-1]['ID'] + 1

        usuarios.append(usuario)
    else:
        print(usuarios)
        repeticao = False

    


   





