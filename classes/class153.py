class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instancia')
        return super().__new__(cls)

    def __init__(self, x):
        self.x = x
        print('Sou o init')
    
    def __repr__(self):
        return f'A()'
    
a = A(123)
print(a.x)