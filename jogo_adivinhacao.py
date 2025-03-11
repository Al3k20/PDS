# Importa o módulo random, que contém funções para gerar números aleatórios
import random

# Gera um número aleatório entre 1 e 10 e o armazena na variável numero_secreto
# O jogador tentará adivinhar este número
numero_secreto = random.randint(1, 10)

# Inicializa o número de tentativas como 0, para começar a contagem
tentativas = 0

# Define o número máximo de tentativas permitidas para o jogador
max_tentativas = 5

# Imprime mensagens de boas-vindas e explica o objetivo do jogo ao jogador
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Inicia o loop do jogo, que continuará enquanto o jogador ainda tiver tentativas disponíveis
while tentativas < max_tentativas:
    # Solicita ao jogador que insira seu palpite e converte a entrada para um número inteiro
    palpite = int(input("Digite seu palpite: "))

    # Incrementa o número de tentativas em 1, pois o jogador fez uma tentativa
    tentativas += 1

    # Verifica se o palpite do jogador está correto
    if palpite == numero_secreto:
        # Se o jogador acertar, exibe uma mensagem de sucesso com o número de tentativas utilizadas
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break  # Encerra o loop, já que o jogador acertou
    elif palpite < numero_secreto:
        # Caso o palpite seja menor que o número secreto, fornece uma dica para tentar um número maior
        print("Quase lá! Tente um número maior.")
    else:
        # Caso o palpite seja maior que o número secreto, fornece uma dica para tentar um número menor
        print("Quase lá! Tente um número menor.")

    # Informa ao jogador quantas tentativas ainda restam
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# Se o jogador não adivinhar o número dentro do número máximo de tentativas
else:
    # Exibe uma mensagem informando que o jogador perdeu e revela o número secreto
    print("Infelizmente, você não acertou. O número era", numero_secreto)
    print("Fim do jogo!")  # Final