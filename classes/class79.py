import copy

d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0, 3, 4]
}
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999
print(d1)
print(d2)