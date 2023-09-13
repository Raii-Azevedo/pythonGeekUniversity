import random

# Inicialização do score
score_jogador = 0
score_computador = 0

while True:
    # Opções disponíveis
    opcoes = ["Pedra", "Papel", "Tesoura"]

    # Computador escolhe aleatoriamente
    escolha_computador = random.randint(0, 2)

    # Exibição das opções para o jogador
    print("Escolha uma opção:")
    for i, opcao in enumerate(opcoes):
        print(f"{i + 1}: {opcao}")

    # Jogador faz sua escolha
    escolha_jogador = int(input("Digite o número da sua escolha (1/2/3): ")) - 1

    # Verificação de quem ganhou
    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == 0 and escolha_computador == 2) or \
         (escolha_jogador == 1 and escolha_computador == 0) or \
         (escolha_jogador == 2 and escolha_computador == 1):
        print("Você ganhou!")
        score_jogador += 1
    else:
        print("O computador ganhou!")
        score_computador += 1

    # Exibe o placar
    print(f"Placar: Jogador {score_jogador} - {score_computador} Computador")

    # Pergunta se o jogador deseja continuar
    continuar = input("Deseja jogar novamente? (s/n): ")
    if continuar.lower() != 's':
        break

print("Fim do jogo!")
