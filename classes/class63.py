cpf_inserido = input('Digite o CPF: ')
cpf_formado = ''
soma_valores_1d = 0
soma_valores_2d = 0
regressor_1d = 10
regressor_2d = 11

for valor in cpf_inserido:
    if valor == '-':
        cpf_formado += valor
        break
    elif valor == '.':
        cpf_formado += valor
        continue
    else:
        try:
            cpf_formado += valor
            valor_int = int(valor)
            soma_valores_1d += valor_int * regressor_1d
            soma_valores_2d += valor_int * regressor_2d
            regressor_1d -= 1
            regressor_2d -= 1
        except:
            print(f'Valor "{valor}" não reconhecido')

primeiro_digito = (soma_valores_1d*10)%11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

soma_valores_2d += primeiro_digito * regressor_2d
segundo_digito = (soma_valores_2d*10)%11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_formado += str(primeiro_digito) + str(segundo_digito)

if cpf_formado == cpf_inserido:
    print(f'O CPF {cpf_inserido} é válido')
else:
    print(f'O CPF inserido não é válido')