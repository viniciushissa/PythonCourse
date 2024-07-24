a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.7,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

# (a1, a2), b = pessoa.items()
# print(a1, a2, b)

# for chave, valor in pessoa.items():
#     print(chave, valor)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(args)
    for item, valor in kwargs.items():
        print(item,valor)

mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
mostro_argumentos_nomeados(**pessoa_completa)