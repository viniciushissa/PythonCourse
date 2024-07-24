def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Luiz'))
print(falar_boa_noite('Vinicius'))

for nome in ['Maria', 'Joana', 'Luiz', 'Jonas']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))