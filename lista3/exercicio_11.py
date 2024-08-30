import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Variável para armazenar o palpite do usuário
palpite = None

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

# Loop para continuar o jogo até o usuário acertar
while palpite != numero_secreto:
    # Solicita ao usuário um palpite
    palpite = int(input("Digite seu palpite: "))

    # Verifica se o palpite é maior, menor ou igual ao número secreto
    if palpite < numero_secreto:
        print("Seu palpite é menor do que o número secreto. Tente novamente!")
    elif palpite > numero_secreto:
        print("Seu palpite é maior do que o número secreto. Tente novamente!")
    else:
        print(f"Parabéns! Você acertou! O número secreto era {numero_secreto}.")