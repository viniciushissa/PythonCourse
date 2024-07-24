def mult(*args):
    total = 1
    for num in args:
        total *= num
    return total

def par_ou_impar(num):
    if num % 2 == 0:
        return 'Par'
    return 'Ímpar'

multiplicacao = mult(2, 4, 6, 8, 10)
print(multiplicacao)

result1 = par_ou_impar(19)
result2 = par_ou_impar(14)
print(result1)
print(result2)