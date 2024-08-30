def lista_de_compras():
    lista = []
    while True:
        item = input("Adicione um item à lista de compras (ou digite 'sair' para finalizar): ")
        if item.lower() == 'sair':
            break
        lista.append(item)
    print("\nSua lista de compras:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

# Executa a função
lista_de_compras()