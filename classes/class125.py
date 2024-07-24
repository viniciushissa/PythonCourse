def soma(a, b, /, x, y):
    print(a + b + x + y)

def soma2(a, b, *, c):
    print(a + b + c)

soma(1, 2, 3, y=3)

soma2(1, 2, c=3)
