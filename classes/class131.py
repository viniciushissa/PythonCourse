class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'João', 'idade': 19} 
p1 = Pessoa(**dados)
# p1.nome = 'EITA'
# print(p1.nome)
# print(p1.__dict__)
print(vars(p1))
