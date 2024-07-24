s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update('Olá Mundo')
s1.update(('Olá', 1, 2, 3, 4))

print(s1)

s1.discard('Olá')
print(s1)

s1.clear()