def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(inicio, fim):
    primos = []
    for num in range(inicio, fim + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

# Solicita o intervalo ao usuário
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fm do intervalo: "))

# Encontra e imprime os números primos no intervalo
primos = encontrar_primos(inicio, fim)
print("Números primos no intervalo:", primos)