from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1000000
data_inicio = datetime.strptime('20/12/2020', '%d/%m/%Y')
delta_anos = relativedelta(years=5)
data_final = data_inicio + delta_anos

data_parcelas = []
data_parcela = data_inicio

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(month=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_emprestimo / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R${valor_parcela:,.2f}')

print()
print(f'Voce pegou R${valor_emprestimo:,.2f} para pagar '
      f'em {delta_anos.years} anos'
      f'({numero_parcelas} meses) em parcelas de '
      f'R${data_parcelas:,.2f}')