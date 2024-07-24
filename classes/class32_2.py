hora_str = input('Digite a hora em números inteiros: ')

try:
    hora_int = int(hora_str)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >= 18 and hora_int <=23:
        print('Boa noite')
    else:
        print('Nao conheço essa hora')
except:
    print('Digite apenas numeros inteiros')