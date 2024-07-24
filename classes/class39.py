nome = 'Luiz Otávio'
indice = 0
novo_nome = ''
tamnome = len(nome)

while indice < tamnome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)