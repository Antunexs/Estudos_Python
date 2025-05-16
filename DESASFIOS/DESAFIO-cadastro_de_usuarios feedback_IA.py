# Cadastro de usuários
'''
Crie um sistema simples de cadastro de usuários utilizando dicionários dentro de uma lista.
Você deve inserir os seguintes dados:
- ID (gerado automaticamente)
- Nome
- Idade
- E-mail
'''

print("=== Cadastro de Usuário ===\n")

usuarios = []
id_atual = 1  # Controla o ID automaticamente

while True:
    resposta = input("Deseja cadastrar um usuário? (S/N): ").strip().upper()

    if resposta == 'S':
        nome = input("Nome: ").strip()
        idade = input("Idade: ").strip()
        email = input("E-mail: ").strip()

        usuario = {
            "ID": id_atual,
            "Nome": nome,
            "Idade": idade,
            "Email": email
        }

        usuarios.append(usuario)
        print(f"\nUsuário '{nome}' cadastrado com sucesso! ID: {id_atual}\n")
        id_atual += 1

    elif resposta == 'N':
        print("\nLista de usuários cadastrados:")
        for u in usuarios:
            print(u)
        break

    else:
        print("Opção inválida. Digite apenas 'S' para sim ou 'N' para não.\n")
