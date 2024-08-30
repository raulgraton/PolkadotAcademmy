def exibir_tabuada(numero):
    # Itera de 1 a 10 e exibe a tabuada
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    # Solicita um número inteiro ao usuário
    while True:
        try:
            numero = int(input("Digite um número para exibir a tabuada: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Exibe a tabuada do número fornecido
    exibir_tabuada(numero)

    main()