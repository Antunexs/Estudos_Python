# Funções e métodos
'''
def nome(parâmetros):
    bloco a ser executado...
    ...
    ...
    return

'''
# var = 'jhlasd'
# print(isinstance(var, int))


def saudacao(nome: str):
    # bloco que será executado
    if isinstance(nome, str):
        print(f'olá, {nome}')
    else:
        print('parâmetro inválido')
    
    
##### EXECUÇÃO #####
# variavel_nome = saudacao('luiz')
# print(type(variavel_nome))

saudacao(12312344)