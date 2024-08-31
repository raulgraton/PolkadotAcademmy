# Inicializa o contador de números positivos
contador_positivos = 0

# Solicita cinco números ao usuário
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    # Verifica se o número é positivo
    if numero > 0:
        contador_positivos += 1

# Exibe o resultado
print(f"Você digitou {contador_positivos} números positivos.")
