class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa('João', 32)
Pessoa.metodo_de_classe()

p2 = Pessoa.criar_com_50_anos('Helena')
print(p2.nome, p2.idade)

p3 = Pessoa.criar_anonimo(18)
print(p3.nome, p3.idade)