from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime(fmt))
print(data.strftime(fmt + ' %H:%M'))
print(data.strftime(fmt + ' %H:%M:%S'))
print(data.strftime('%Y'), data.year)
