# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Exibe a tabuada de multiplicação de 1 a 10
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
