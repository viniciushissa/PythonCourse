def escopo():
    global y
    y = 2
    print(x)
    print(y)
    def outro_escopo():
        z = 3
        print(z)
    outro_escopo()
    

x = 1
y = 10
print(y)
escopo()
print(y)