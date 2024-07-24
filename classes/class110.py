def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

def blablabla(a, b, c):
    print(a, b, c)
    return decoradora

@blablabla(1, 2, 3)
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)