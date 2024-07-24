p1 = {
    'nome' : 'Luiz Otávio',
    'sobrenome' : 'Miranda',
}
print(p1.get('nome'))

nome = p1.pop('nome')
print(nome)
print(p1)

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

p1.update({
    'nome' : 'Vinicius',
    'idade' : 30,
})
print(p1)

tupla = (('nome', 'novo valor'), ('idade', 30))
p1.update(tupla)
print(p1)