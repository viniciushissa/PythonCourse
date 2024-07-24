perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5*5',
        'Opções' : ['10', '25', '30', '40'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/4',
        'Opções' : ['2.5', '3', '1.5', '2'],
        'Resposta' : '2.5',
    },
]

acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i+1})',opcao)
    print()

    escolha_str = input('Escolha uma opção: ')
    try: 
        escolha_int = int(escolha_str)
    except:
        print('Errou')
        continue
    
    if escolha_int >= 1 and escolha_int < 4:
        if pergunta['Opções'][escolha_int-1] == pergunta['Resposta']:
            print('Resposta correta!')
            acertos += 1
        else:
            print('Respota errada')
    else:
        print('Errou')

print(f'Voce acertou {acertos} perguntas!')