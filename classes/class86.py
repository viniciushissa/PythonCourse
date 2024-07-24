lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 3, 2, 1],
    [2, 2, 4, 5, 6, 7],
    [1, 2, 3, 1, 2, 3],
    [4, 4, 4, 4, 4, 4],
]

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        
        numeros_checados.add(numero)

    print()
    print()
    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(lista, encontra_primeiro_duplicado(lista))