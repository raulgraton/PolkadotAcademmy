# Solicita ao usuário que insira as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Define os pesos das notas
peso1 = 2
peso2 = 3
peso3 = 5

# Calcula a soma ponderada das notas
soma_ponderada = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)

# Calcula a média ponderada
media_ponderada = soma_ponderada / (peso1 + peso2 + peso3)

# Exibe o resultado
print(f"A média ponderada das notas é: {media_ponderada:.2f}")