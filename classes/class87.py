lista = [4, 32,1 ,34, 6, 6, 5, 21]
lista.sort()
lista.sort(reverse=True)

print(lista)

lista = [
    {'nome' : 'Luiz', 'sobrenome' : 'Miranda'},
    {'nome' : 'Maria', 'sobrenome' : 'Oliveira'},
    {'nome' : 'Joao', 'sobrenome' : 'Gomes'},
    {'nome': 'Aline', 'sobrenome' : 'Souza'},
    {'nome' : 'Vinicius', 'sobrenome' : 'Hissa'}
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

lista_ordenada_nome = sorted(lista, key=lambda item: item['nome'])
lista_ordenada_sobrenome = sorted(lista, key=lambda item: item['sobrenome'])

exibir(lista_ordenada_nome)
exibir(lista_ordenada_sobrenome)