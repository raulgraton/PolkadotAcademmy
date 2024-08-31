import time

# Contagem regressiva de 10 a 0
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)  # Pausa de 1 segundo entre os números

print("Fogo!")
