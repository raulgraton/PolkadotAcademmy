# Inicializa a variável que armazenará a soma
soma_pares = 0

# Loop para iterar pelos números de 1 a 100
for numero in range(1, 101):
    # Verifica se o número é par
    if numero % 2 == 0:
        # Adiciona o número par à soma acumulada
        soma_pares += numero

# Exibe o resultado da soma
print(f"A soma de todos os números pares entre 1 e 100 é: {soma_pares}")