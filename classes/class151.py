class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'
    

p1 = Ponto(1, 2)
p2 = Ponto(89, 41)
print(p1)
print(repr(p2))
print(f'{p2!r}')