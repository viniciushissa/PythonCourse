#nome = 'Vinicius'

#print(nome[2])
#print(nome[0])
#print(nome[-1])

#print('n' in nome)
#print('z' in nome)
#print('cius' in nome)
#print('incu' not in nome)
#print('ini' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')


