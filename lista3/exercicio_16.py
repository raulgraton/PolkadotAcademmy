# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Inicializa a variável que armazenará a soma dos divisores
soma_divisores = 0

# Loop para encontrar os divisores próprios do número (excluindo ele mesmo)
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

# Verifica se a soma dos divisores é igual ao número
if soma_divisores == numero:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")