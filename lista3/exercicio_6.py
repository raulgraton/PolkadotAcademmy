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

def calcular_media_notas():
    total_notas = 0
    soma_notas = 0
    contador_notas = 0

    while True:
        try:
            nota = float(input("Digite uma nota (ou -1 para encerrar): "))
            
            if nota == -1:
                break
            elif nota < 0 or nota > 10:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
                continue
            
            soma_notas += nota
            contador_notas += 1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    if contador_notas > 0:
        media = soma_notas / contador_notas
        print(f"A média das notas é {media:.2f}.")
    else:
        print("Nenhuma nota foi inserida.")

def main():
    calcular_media_notas()

    main()