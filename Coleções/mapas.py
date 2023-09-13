# Mapas é outra forma de se referir a dicionários em Python
# Dicionários em Python são representados por {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre dicionários (como funcionam os Loops)
print(receita)

for chave in receita: # imprimir as chaves do dicionário receita
    print(chave)


for chave in receita: #Imprime o valor correspondente a cada chave
    print(receita[chave])

# MELHORADO
for chave in receita: # Imprime chave e valor
    print(f'Em {chave} recebi R${receita[chave]}')

# Para conhecer todas as chaves
print(receita.keys())

for chave in receita.keys(): # Método de boa prática de programação
    print(receita[chave])

# ACESSANDO VALORES
print(receita.values())

for valor in receita.values():
    print(valor)

# DESEMPACOTAMENTO DE DICIONÁRIOS
print(receita.items()) # Imprime um dicionário com tuplas contendo chave e valor

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# SÓ É POSSÍVEL REALIZAR SOMA DE VALORES, SE TODOS FOREM INTEIROS OU REAIS
print (sum(receita.values()))
print (max(receita.values()))
print (min(receita.values()))
print(len(receita))