def soma_numeros():
    soma = 0
    while True:
        numero = int(input("Digite um número (ou 0 para sair): "))
        if numero == 0:
            break
        soma += numero
    print(f"A soma dos números digitados é: {soma}")

# Executa a função
soma_numeros()