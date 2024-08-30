def ordenar_numeros(a, b, c):
    # Inicializa uma lista com os três números
    numeros = [a, b, c]
    # Ordena a lista em ordem crescente
    numeros.sort()
    return numeros

def main():
    while True:
        try:
            # Solicita três números ao usuário
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            c = float(input("Digite o terceiro número: "))
            
            # Verifica se os números são diferentes
            if a == b or b == c or a == c:
                print("Os números devem ser diferentes. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
    
    # Ordena os números
    numeros_ordenados = ordenar_numeros(a, b, c)
    
    # Exibe os números em ordem crescente
    print(f"Os números em ordem crescente são: {numeros_ordenados}")

# Executa a função principal
main()