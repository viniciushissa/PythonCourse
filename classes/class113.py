def soma_numeros_da_lista(l1, l2):
    tamanho_menor_lista = min(len(l1), len(l2))
    return [
        l1[i] + l2[i] for i in range(tamanho_menor_lista)
    ]

l1 = [1, 2, 3, 4]
l2 = [1, 3, 5, 7, 9, 11]

print(soma_numeros_da_lista(l1, l2))