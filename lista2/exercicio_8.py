def contar_letra(frase, letra):
    contador = frase.lower().count(letra.lower())
    return contador

# Solicita a frase e a letra ao usuário
frase = input("Digite uma frase: ")
letra = input("Digite a letra que deseja contar: ")

# Conta quantas vezes a letra aparece na frase
quantidade = contar_letra(frase, letra)

# Exibe o resultado
print(f"A letra '{letra}' aparece {quantidade} vez(es) na frase.")