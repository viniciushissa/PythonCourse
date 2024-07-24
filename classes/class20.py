primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'o primeiro_valor={primeiro_valor} é maior que o segundo_valor={segundo_valor}')
elif primeiro_valor == segundo_valor:
    print('o primeiro_valor e o segundo_valor são iguais')
else:
    print(f'o segundo_valor={segundo_valor} é maior que o primeiro_valor={primeiro_valor}')