from itertools import groupby

alunos = [
    {'nome' : 'Luiz', 'nota' : 'A'}, 
    {'nome' : 'Leticia', 'nota' : 'B'}, 
    {'nome' : 'Fabricio', 'nota' : 'A'}, 
    {'nome' : 'Rosemary', 'nota' : 'C'}, 
    {'nome' : 'Joana', 'nota' : 'D'}, 
    {'nome' : 'Joao', 'nota' : 'A'}, 
    {'nome' : 'Andre', 'nota' : 'B'}, 
    {'nome' : 'Eduardo', 'nota' : 'A'}, 
    {'nome' : 'Anderson', 'nota' : 'C'}, 
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)