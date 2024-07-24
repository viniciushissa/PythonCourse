try:
    print('ABRIR ARQUIVO')
    7/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU 0')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')