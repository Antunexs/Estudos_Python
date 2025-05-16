funcionario = {
    # "CHAVE": "VALOR" = str, int, true, list, tuple, float"
    "id": 1,
    "nome": "Antunes",
    "idade": 23,
    "is_staff": True,
    "atribuições": ['dev', 'governança', 'suporte'],
    "dict_exemplo": {'chave': 'valor'}

}

print('Id: ', funcionario['id'])
print('nome: ', funcionario['nome'])
print('idade: ', funcionario['idade'])
print('é staff? : ',funcionario['is_staff'])

 # lista dentro do dict
print(funcionario["atribuições"][0])

#print(funcionario["dict"]["chave"])

# métodos de dicionários

print()
print(funcionario.get('nome')) # retorna o valor das chaves
chaves = funcionario.keys() # retorna as chaves
print(chaves)

print()
print(funcionario.values()) # Todos os valores das chaves
print()
print(funcionario.items()) # Retorna chave e valor 
print()
funcionario.pop('is_staff') # deleta a chave
print(funcionario.items())
print()

funcionario.update({"local": 'BLOCO H - DTI'}) # adiciona uma chave ao final 
print(funcionario.items())
