numero_str = input('Digite um numero inteiro: ')

try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print(f'{numero_int} é par')
    else:
        print(f'{numero_int} é ímpar')
except:
    print(f'{numero_str} não é um número inteiro')