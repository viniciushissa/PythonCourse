while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operacao = input('Digite a opereção [+] [-] [*] [/]: ')

    num_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_validos = True
    except:
        num_validos = None
    
    if num_validos is None:
        print('Um ou ambos os números digitados sao invalidos')
        continue

    operadores_permiditos = '+-/*'
    if operacao not in operadores_permiditos:
        print('Operador não permitidos')
        continue
    
    if len(operacao) > 1:
        print('Digite apenas um operador')
        continue
    
    if operacao == '+':
        print(f'{num1} + {num2} = {num1_float + num2_float}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1_float - num2_float}')
    elif operacao == '*':
        print(f'{num1} * {num2} = {num1_float * num2_float}')
    elif operacao == '/':
        print(f'{num1} / {num2} = {num1_float / num2_float}')
    else:
        print('Operação não reconhecida!')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break

print('Finalizado!')