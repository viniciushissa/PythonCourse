condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor' if True else 'Outro Valor' if True else 'Fim')
print('Valor' if False else 'Outro Valor' if True else 'Fim')
print('Valor' if False else 'Outro Valor' if False else 'Fim')