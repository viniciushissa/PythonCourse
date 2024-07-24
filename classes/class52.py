lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)

lista_b = lista_a.copy()
print(lista_b)