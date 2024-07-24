def multiplos(num):
    for indice in range(2,5):
        print(f'{num}x{indice} = {num*indice}')


numero = int(input('Digite um número que deseja saber os múltiplos: '))
multiplos(numero)