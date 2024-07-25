import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(Depósito ${valor})')
        return self.saldo
    
    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é ${self.saldo:.2f} {msg} \n--')
    
class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Sacando ${valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(Saque Negado ${valor})')
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name} {attrs}'


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo:float = 0, limite:float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(Sacando ${valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é ${-self.limite:.2f}')
        self.detalhes(f'(Saque Negado ${valor})')
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite})'
        return f'{class_name} {attrs}'