import contas, pessoa, banco

c1 = pessoa.Cliente('Luiz', 30)
cc1 = contas.ContaCorrente(111, 222, 0, 0)
c1.conta = cc1
c2 = pessoa.Cliente('Maria', 18)
cp1 = contas.ContaPoupanca(112, 223, 100)
c2.conta = cp1
banco = banco.Banco()
banco.clientes.extend([c1, c2])
banco.contas.extend([cc1, cp1])
banco.agencias.extend([111, 112, 222])

print(banco.autenticar(c1, cp1))
print(banco.autenticar(c1, cc1))

print(banco)

if banco.autenticar(c1, cc1):
    cc1.depositar(10)
    c1.conta.depositar(100)
    cc1.sacar(20)
    print(c1.conta)