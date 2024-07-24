import os

palavra_secreta = 'cachorro'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    tentativas += 1 
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_atual in palavra_secreta:
        if letra_atual in letras_acertadas:
            palavra_formada += letra_atual
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Voce ganhou! O número de tentativas foi de {tentativas}x.')
        print('Continue digitando para recomeçar. Mude a palavra secreta caso queira.')
        letras_acertadas = ''
        tentativas = 0