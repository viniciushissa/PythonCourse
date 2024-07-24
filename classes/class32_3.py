nome = input('Digite seu nome: ')
lennome = len(nome)

if lennome > 1:
    if lennome <= 4:
        print('Seu nome é curto')
    elif lennome >= 5 or lennome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')