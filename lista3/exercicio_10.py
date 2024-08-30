import math

# Solicita ao usuário o valor do raio
raio = float(input("Digite o raio do círculo: "))

# Calcula a área usando a fórmula A = πr²
area = math.pi * raio ** 2

# Exibe o resultado
print(f"A área do círculo com raio {raio} é: {area:.2f}")