# Solicita a temperatura em graus Celsius ao usuário
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte Celsius para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibe o resultado da conversão
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
