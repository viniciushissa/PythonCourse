def nao_aceito_zero(d):
    if d == 0: 
        raise ZeroDivisionError('Voce esta tentando dividir por 0')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(f'{n} deve ser int ou float! {tipo_n.__name__} enviado')
    return True

def divide (n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, '0'))