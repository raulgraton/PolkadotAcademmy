def gerar_fibonacci(n):
    # Verifica se o número de termos é válido
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Inicializa os primeiros dois números da sequência
    fibonacci = [0, 1]
    
    # Gera a sequência de Fibonacci até o enésimo termo
    while len(fibonacci) < n:
        proximo_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_numero)
    
    return fibonacci

def main():
    # Solicita o número de termos ao usuário
    while True:
        try:
            n = int(input("Digite o número de termos da sequência de Fibonacci: "))
            if n < 0:
                print("O número de termos deve ser um inteiro não-negativo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    # Gera a sequência de Fibonacci
    fibonacci = gerar_fibonacci(n)
    
    # Exibe a sequência de Fibonacci
    print(f"A sequência de Fibonacci com {n} termos é: {fibonacci}")

main()