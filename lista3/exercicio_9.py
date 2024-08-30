def verificar_paridade(numero):
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    while True:
        try:
            # Solicita um número inteiro ao usuário
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    # Verifica a paridade do número
    paridade = verificar_paridade(numero)
    
    # Exibe o resultado
    print(f"O número {numero} é {paridade}.")

if _name_ == "_main_":
    main()