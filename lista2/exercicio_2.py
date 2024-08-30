# Programa para calcular e exibir operações básicas entre dois números

# Solicita ao usuário o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário o segundo número
num2 = float(input("Digite o segundo número: "))

# Calcula as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verifica se o segundo número não é zero antes de tentar dividir
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Divisão por zero não é permitida"

# Exibe os resultados
print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
print(f"Divisão: {num1} / {num2} = {divisao}")