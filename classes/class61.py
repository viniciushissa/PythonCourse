string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, *_, u = lista
print(a, u)

for nome in lista:
    print(nome)

print('\n -----------------------')
print(*lista)
print(*string)
print(*tupla)