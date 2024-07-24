import os

caminho_arquivo = 'C:\\!devProjects\\Python Course\\'
caminho_arquivo += 'class121.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     arquivo.seek(0, 0)
#     print(arquivo.readline())
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
#     print()

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo:
#     arquivo.write('Atenção\n')
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )

# os.remove(caminho_arquivo)
# os.unlin
# os.rename(caminho_arquivo, 'class121-renamed.txt')