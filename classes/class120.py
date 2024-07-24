# def recursiva(inicio=0, fim=10):
#     if inicio >= fim:
#         return 'Acabou'

#     print(inicio)
#     inicio += 1
#     return recursiva(inicio, fim)

# recursiva()

def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n - 1)

print(fatorial(5))
    
