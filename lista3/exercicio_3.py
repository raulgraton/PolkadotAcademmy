def verificar_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto = ''.join(c.lower() for c in texto if c.isalnum())
    # Compara o texto com sua versão invertida
    return texto == texto[::-1]

def main():
    # Solicita uma palavra ou frase ao usuário
    entrada = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    
    # Verifica se a entrada é um palíndromo
    if verificar_palindromo(entrada):
        print("A entrada é um palíndromo.")
    else:
        print("A entrada não é um palíndromo.")

    main()