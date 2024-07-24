lista = []

while True:
    opcao = input('Selecione uma opção: \n[i]nserir [a]pagar [l]istar\n')
    if opcao == 'i':
        produto_inserido = input('Insira o nome do produto: ')
        if produto_inserido == '':
            print('Nada listado')
            continue
        else:
            lista.append(produto_inserido)
    elif opcao == 'a':
        indice_str = input('Insira o indice do produto que deseja apagar: ')
        indice = int(indice_str)
        if indice_str == '':
            print('Indice não inserido')
            continue
        else:
            del lista[indice]
    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada listado')
        else:
            for i, valor in enumerate(lista):
                print(i, valor)
    else:
        print('Digite uma opção correta')