# Inicializa uma lista vazia para armazenar os números
numeros = []

# Solicita ao usuário que insira números até ele decidir parar
print("Digite os números para a lista. Para finalizar, digite 'sair'.")

while True:
    entrada = input("Digite um número ou 'sair' para finalizar: ")

    if entrada.lower() == 'sair':
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido ou 'sair'.")

# Verifica se a lista não está vazia antes de calcular
if numeros:
    # Calcula o maior número
    maior_numero = max(numeros)

    # Calcula o menor número
    menor_numero = min(numeros)

    # Calcula a média dos números
    media_numeros = sum(numeros) / len(numeros)

    # Exibe os resultados
    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")
    print(f"Média dos números: {media_numeros:.2f}")
else:
    print("Nenhum número foi inserido.")