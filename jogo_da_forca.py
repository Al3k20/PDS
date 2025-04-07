def desenhar_forca(erros):
    partes_do_corpo = [
        " O ",       # Cabeça
        "/|\\",      # Tronco e braços
        " | ",       # Corpo
        "/ \\",      # Pernas
    ]
    print("\n")
    print(" ----- ")
    print(" |   | ")
    if erros > 0:
        print(" |   " + partes_do_corpo[0] if erros >= 1 else " |")
    if erros > 1:
        print(" |  " + partes_do_corpo[1] if erros >= 2 else " |")
    if erros > 2:
        print(" |   " + partes_do_corpo[2] if erros >= 3 else " |")
    if erros > 3:
        print(" |  " + partes_do_corpo[3] if erros >= 4 else " |")
    print(" |")
    print("=======\n")


# Código aprimorado do jogo
palavra_secreta = "girafa".lower()
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6
erros = 0

print("Bem-vindo ao jogo da forca!")
desenhar_forca(erros)
print(" ".join(letras_acertadas))

while tentativas > 0 and "_" in letras_acertadas:
    palpite = input("\nDigite uma letra: ").lower()

    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, insira apenas uma letra.")
        continue

    if palavra_secreta.count(palpite) > 0:
        for index in range(len(palavra_secreta)):
            if palavra_secreta[index] == palpite:
                letras_acertadas[index] = palpite
        print("\nBoa! Você acertou uma letra!")
    else:
        erros += 1
        tentativas -= 1
        print(f"\nOps! Letra errada. Você tem {tentativas} tentativas restantes.")
        desenhar_forca(erros)

    print("Palavra: " + " ".join(letras_acertadas))

if "_" not in letras_acertadas:
    print("\nParabéns, você ganhou!")
else:
    print("\nQue pena, você perdeu. A palavra era:", palavra_secreta)
