try:
    a = 18
    b = 0
    print('Linha 1'[100])
    c = a / b
except ZeroDivisionError:
    print('Dividiu por 0')
except NameError as error:
    print('Nome b não está definido')
    print('MSG: ', error)

except Exception:
    print('ERRO DESCONHECIDO.')