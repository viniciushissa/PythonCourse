a = 'A'
b = 'B' 
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c)

print(formato)

formato = 'a={0} a={0} a={0} b={1} c={2:.2f}'.format(a, b, c)

print(formato)

formato = 'a={0} a={0} a={0} b={1} c={nome3:.2f}'.format(a, b, nome3=c)

print(formato)