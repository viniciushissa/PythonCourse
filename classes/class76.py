pessoa = {
    'nome' : 'Luiz Otávio',
    'sobrenome' : 'Miranda',
    'idade' : 18,
    'altura' : 1.8,
    'endereços' : [
        {'rua': 'tal tal', 'numero' : 123},
        {'rua': 'outral', 'numero' : 456},
    ],
}

print(pessoa['nome'])
print(pessoa['endereços'])

for chave in pessoa:
    print(chave, pessoa[chave])