def calcular_fatorial(n):
    # Inicializa o resultado como 1
    resultado = 1
    # Loop para multiplicar os números de n até 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def main():
    # Solicita um número inteiro ao usuário
    while True:
        try:
            numero = int(input("Digite um número inteiro para calcular o fatorial: "))
            if numero < 0:
                print("Por favor, digite um número inteiro não-negativo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Calcula o fatorial usando a função
    fatorial = calcular_fatorial(numero)
    
    # Exibe o resultado
    print(f"O fatorial de {numero} é {fatorial}.")

main()