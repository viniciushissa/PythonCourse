pessoa = {
    'nome' : 'Luiz Otávio',
    'sobrenome' : 'Miranda',
}

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

pessoa.setdefault('idade', 0)
print(pessoa['idade'])