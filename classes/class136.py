# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor    


# caneta = Caneta('Azul')
# print(caneta.get_cor())

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 'RGB'

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)