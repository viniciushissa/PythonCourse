def saudacao(msg, nome, msg2):
    return f'{msg}, {nome}. {msg2}'

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Bom dia', 'Vinicius', 'Está muito calor hoje!')
print(v)