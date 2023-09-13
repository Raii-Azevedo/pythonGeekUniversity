# Definindo um conjunto:
# FORMA 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) #Note que há valores repetidos
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, ele é ignorado sem gerar erros e não fará parte do conjunto

# FORMA 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')
# Pode verificar se o elemento está contindo no conjunto

'''IMPORTANTE lembrar que: Além de não ter vlaores duplicados, não tem ordem em conjuntos (set)'''

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos\n')

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos\n')

# Transformando conjunto em dicionário
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict') # Dicionário não repete chaves
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos\n')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')
