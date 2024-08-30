def converter_temperaturas(celsius):
    # Converte Celsius para Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    # Converte Celsius para Kelvin
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

def main():
    # Solicita a temperatura em Celsius ao usuário
    while True:
        try:
            celsius = float(input("Digite a temperatura em Celsius: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Converte a temperatura usando a função
    fahrenheit, kelvin = converter_temperaturas(celsius)
    
    # Exibe os resultados
    print(f"{celsius} graus Celsius é igual a {fahrenheit:.2f} graus Fahrenheit.")
    print(f"{celsius} graus Celsius é igual a {kelvin:.2f} Kelvin.")

if _name_ == "_main_":
    main()