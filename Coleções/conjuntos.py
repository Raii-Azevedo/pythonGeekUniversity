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

# Listas aceitam valores duplicados (10 elementos)
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos\n')

# Tuplas aceitam valores duplicados (10 elementos)
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos\n')

# Transformando conjunto em dicionário
# Dicionários não aceitam chaves duplicadas
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict') # Dicionário não repete chaves
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos\n')

# Conjuntos não aceitam valores duplicados
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


# SETS

'''Imagine um formulário de cadastro de visitantes em um feira ou museu
onde os visitantes informam manualmente a cidade que residem, 

-> Adicionamos cada cidade em uma lista Python (a lista pode adicionar novos elementos através do append)
e ter repetições.'''

cidades = ['Belo Horizonte', 'Campo Grande', 'Vitória', 'São Paulo', 'Campo Grande', 'Vitória']
print(cidades)

# Para saber somente a quantidade de pessoas que visitou o museu
print(len(cidades))

# Agora saber quantas cidades distintas (únicas) tem
'O que fazer? Loop na lista para verificar e tirar repetições?'

# UTILIZAR SET
print(len(set(cidades)))
print (set(cidades))

'O set vai pegar a lista e tranformar num set e remover automáticamente a duplicidade.'

# SOBRE ORDENAÇÃO: O conjunto não mantem a ordem de colocação dos valores, ele faz uma ordem própria.

'Adicionando elementos em um conjunto'

s = {1, 2, 3}
s.add(4)  # Ou seja, conjuntos são mutáveis.
s.add(4)  # Duplicidade não gera erro, simplemente é ignorado e não adicionado
print(s)


'Removendo elementos em um conjunto'
# FORMA 1

s.remove(3) # NÃO É INDICE, o valor 3 foi removido, e não o valor na Terceira posição
print(s)  # OBS. Se indicar um valor que não exista no set, vai gerar um erro (KeyError). Não retorna valores também.

# FORMA 2

ret = s.discard(2) # No DISCARD, se tentar remover um elemento que não está no set, não gera erro. Apenas não remove nada.
print(ret) # Também não retorna o valor eliminado
print(s,'\n')

'Copiando um conjunto para outro'

s = {4, 2, 3}
# FORMA 1 - DEEP COPY (Gera objetos independentes)

novo =  s.copy()
print(s)

novo.add(6)
print(novo)
print(s,'\n') # O conjunto original se mantém


# FORMA 2 - SHALLOW COPY
novo = s   # Essa não aloca um novo espaço da memória

novo.add(8)
print(novo) # Ambos novo e S serão modificados.
print(s, '\n')

'Podemos remover TODOS os ítens de um conjunto'
# Utilizando o CLEAR

s.clear()
print(s,'\n')  # Retorna set() - > Que indica conjunto vazio.

#  MÉTODOS MATEMÁTICOS DE CONJUNTOS

'''Imagine que há 2 conjuntos: Um contendo estudantes do curso de Python
e outro com estudantes do curso de java'''

estudantes_python = {'Marcos', 'Patrícia', 'Raíssa', 'Gustavo', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Júlia', 'Gustavo', 'Ana'}

# Alguns alunos estudam nas duas turmas

'É necessário gerar um conjunto com nomes de estudantes únicos'
# FORMA 1 - Utilizando UNION (Recurso da matemática)

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1,'\n')

# FORMA 2 - Utilizando o caractere PIPE   |

unicos2 = estudantes_python | estudantes_java
print(unicos2, '\n')

'Gerar um conjunto de estudantes que estão em ambos os cursos'

# FORMA 1 - Utilizando INTERSECTION (método matemático)

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1, '\n')

# FORMA 2 -  Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2,  '\n')


'Gerar um conjunto de estudantes de um curso que não estão no outro'
so_python = estudantes_python.difference(estudantes_java)
print(f' Só estudam Python: {so_python}')

so_java = estudantes_java.difference(estudantes_python)
print(f' Só estudam Java: {so_java} \n')

# Soma*, Valor Máximo*, Valor minimo*, Tamanho (SE OS VALORES FOREM INTEIROS OU REAIS)

s = {1, 2, 3, 4, 5, 6}
print(s)
print(f'Soma: {sum(s)}')
print(f'Máximo: {max(s)}')
print(f'Mínimo: {min(s)}')
print(f'Tamanho: {len(s)}')







