lista = ['Maria', 'Helena', 'Liuz']
lista.append('Joao')

lista_enumerada = enumerate(lista)
print(lista_enumerada)

for item in lista_enumerada:
    print(item)