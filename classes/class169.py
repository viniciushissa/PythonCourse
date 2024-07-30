from datetime import datetime
from pytz import timezone

# data_str_data = '2022-04-20 07:49:23'
# data_str_data = '20/04/2022'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'
# data_str_fmt = '%d/%m/%Y'

# data = datetime.strptime(data_str_data, data_str_fmt)
# data = datetime(2022, 4, 20, 7, 49, 23)

# data = datetime.now(timezone('America/Sao_Paulo'))
# print(data)

# data = datetime.now(timezone('Asia/Tokyo'))
# print(data)

data = datetime.now()
data_now = data.timestamp()
print(datetime.fromtimestamp(data_now))