class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome):
        print(nome, 'Chamando,', self.phone)
        return 2134

call1 = CallMe('28388328')
retorno = call1('Vinicius')
print(retorno)