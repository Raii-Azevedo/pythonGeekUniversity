# ESTRUTURA CONDICIONAL LÓGICA: AND OR NOT IS

'''
REGRAS DE FUNCIONAMENTO
Para o AND ambos ou todos os valores precisam ser TRUE
Para o OR, apenas 1 dos valores precisa ser TRUE
Para o NOT o valor do Boleano(True/False) é invertido
'''

ativo = True
logado = True

if ativo and logado:
    print("Bem vindo ao sistema")
else:
    print('Você precisa ativar sua conta.POr favor, cheque seu e-mail')

