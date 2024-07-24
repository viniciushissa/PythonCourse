pessoa = {}

pessoa['nome'] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa)
print(pessoa['nome'])
print(pessoa['sobrenome'])
del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
