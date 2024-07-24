import random

nove_digitos = ''
cpf_formado = ''
soma_valores_1d = 0
soma_valores_2d = 0
regressor_1d = 10
regressor_2d = 11

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

for valor in nove_digitos:
    cpf_formado += valor
    valor_int = int(valor)
    soma_valores_1d += valor_int * regressor_1d
    soma_valores_2d += valor_int * regressor_2d
    regressor_1d -= 1
    regressor_2d -= 1

primeiro_digito = (soma_valores_1d*10)%11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

soma_valores_2d += primeiro_digito * regressor_2d
segundo_digito = (soma_valores_2d*10)%11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_formado += str(primeiro_digito) + str(segundo_digito)

print(f'O CPF formado foi {cpf_formado[0:3]}.{cpf_formado[3:6]}.{cpf_formado[6:9]}-{cpf_formado[9:]}')