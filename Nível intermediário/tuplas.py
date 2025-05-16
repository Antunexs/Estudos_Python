tupla = (0, 1, 2, 'string', True)
tupla_letras = 'a', 'b', 'c'

print(type(tupla))
print(type(tupla_letras))

for i in tupla:
    print(i)

print(tupla_letras[0])
# tupla_letras[0] = 'd' -> NÃO PODE!!!

# Transformando tupla em lista
tuple_to_list = list(tupla_letras)
tuple_to_list.append('d')
print(tuple_to_list)

# transformar em tupla
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)
print(type(list_to_tuple))

# métodos
print(list_to_tuple.count('b'))
print(list_to_tuple.index('d'))
