# Programa para classificar a temperatura atual

# Solicita ao usuário a temperatura atual
temperatura = float(input("Digite a temperatura atual em graus Celsius: "))

# Classifica a temperatura e exibe a mensagem correspondente
if temperatura > 30:
    print("Está quente.")
elif temperatura < 15:
    print("Está frio.")
else:
    print("Está agradável.")