entrada = input('[E]ntrar [S]air: ')
senha_permitida = '123456'

if entrada == 'E' or entrada == 'e':
    senha_digitada = input('Senha: ')
    if senha_digitada == senha_permitida:
        print('Entrar')
    else:
        print('Senha incorreta')
else: 
    print('Sair')