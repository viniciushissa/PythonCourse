string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break


    print(letra)
    i += 1
else:
    print('Nao encontrei espaço na string')

print('Fora do while')