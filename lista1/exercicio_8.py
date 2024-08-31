# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Calcula o fatorial do número
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    
    # Exibe o resultado
    print(f"O fatorial de {numero} é: {fatorial}")
