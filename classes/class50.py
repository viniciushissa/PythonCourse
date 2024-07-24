lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
print(lista, nome)

lista.append(1233)
del lista[-1]
print(lista)

lista.insert(0, 99)
print(lista)