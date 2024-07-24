import importlib

import class104_m

print(class104_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(class104_m)

print('FIM')