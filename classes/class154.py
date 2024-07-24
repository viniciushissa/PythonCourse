# with open('aula154.txt', 'w', encoding='utf8') as arquivo:
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
        print('INIT')

    def __enter__(self):
        print('ENTER')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('EXIT')
        self._arquivo.close()

        # raise class_exception('Minha mensagem')

        # exception_.add_note('Minha Nota')

        # raise ConnectionError('Não deu pra conectar')


with MyOpen('class154.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)