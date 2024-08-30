# Solicita ao usuário que insira uma string
texto = input("Digite uma string: ")

# Inicializa uma variável para armazenar a string invertida
texto_invertido = ""

# Loop para percorrer a string de trás para frente
for char in texto:
    texto_invertido = char + texto_invertido

# Exibe a string invertida
print(f"A string invertida é: {texto_invertido}")