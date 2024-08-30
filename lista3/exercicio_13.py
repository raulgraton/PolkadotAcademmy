# Solicita ao usuário o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário o segundo número
numero2 = float(input("Digite o segundo número: "))

# Solicita ao usuário o operador desejado
operador = input("Digite a operação (+, -, *, /): ")

# Realiza a operação correspondente e exibe o resultado
if operador == "+":
    resultado = numero1 + numero2
    print(f"O resultado de {numero1} + {numero2} é: {resultado}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"O resultado de {numero1} - {numero2} é: {resultado}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"O resultado de {numero1} * {numero2} é: {resultado}")
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado de {numero1} / {numero2} é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida!")
else:
    print("Operador inválido! Por favor, digite +, -, *, ou /.")