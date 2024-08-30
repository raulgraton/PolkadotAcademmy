def calcular_imc(peso, altura):
    # Calcula o IMC usando a fórmula fornecida
    imc = peso / (altura * altura)
    return imc

def main():
    # Solicita o peso e a altura ao usuário
    while True:
        try:
            peso = float(input("Digite o peso em quilogramas (kg): "))
            altura = float(input("Digite a altura em metros (m): "))
            if peso <= 0 or altura <= 0:
                print("O peso e a altura devem ser valores positivos. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

    # Calcula o IMC usando a função
    imc = calcular_imc(peso, altura)
    
    # Exibe o resultado
    print(f"O Índice de Massa Corporal (IMC) é {imc:.2f}.")

    main()