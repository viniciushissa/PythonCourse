lista = [10, 20, 30, 40]
print(lista)

lista[2] = 5
print(lista)

numero = lista[3]
print(numero)

del lista[2]
print(lista)

lista.append(2)
print(lista)

lista.sort()
print(lista)

ultimo_valor = lista.pop(2)
print(lista)
print('Valor removido', ultimo_valor)