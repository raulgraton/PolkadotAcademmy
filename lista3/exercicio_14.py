# Solicita ao usuário o valor de n
n = int(input("Digite um número natural n: "))

# Inicializa a variável que armazenará a soma
soma = 0

# Loop para iterar de 1 até n
for i in range(1, n + 1):
    # Acumula a soma dos números
    soma += i

# Exibe o resultado da soma
print(f"A soma dos primeiros {n} números naturais é: {soma}")