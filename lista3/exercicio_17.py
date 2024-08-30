# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Divide a frase em palavras usando o método split()
palavras = frase.split()

# Conta o número de palavras na lista
numero_palavras = len(palavras)

# Exibe o resultado
print(f"A frase contém {numero_palavras} palavras.")