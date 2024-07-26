# from collections import namedtuple

# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE'],
# )

from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'

as_espadas = Carta('A', 'Espadas')
print(as_espadas)
print(as_espadas.naipe)
print(as_espadas.valor)

print()
print(as_espadas._fields)
print(as_espadas._field_defaults)

print()
print(as_espadas._asdict())