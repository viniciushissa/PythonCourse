class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome):
        self._motor = nome

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

c1 = Carro('P1')
mclaren = Fabricante('McLaren')
v6 = Motor('V6')
c1.fabricante = mclaren
c1.motor = v6
print(c1.nome, c1.motor.nome, c1.fabricante.nome)