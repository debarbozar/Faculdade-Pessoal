"""
Jogo de adivinhação
"""

secreta = 'segredo'
digitadas = []
chances = 6

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('AH, isso não vale! Digita apenas uma letra :( ')
        continue

    digitadas.append(letra)
    if letra in secreta:
        print(f'UHUUUUUUUL, a letra "{letra}" existe na palavra secreta! ')
    else:
        print(f'AFFFFFF, a letra "{letra}" NÃO EXISTE na palavra secreta :( ')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreta:
         if letra_secreta in digitadas:
             secreto_temporario += letra_secreta
         else:
             secreto_temporario += '*'

    if secreto_temporario == secreta:
        print(f'AGORA SIM HEIN, GANHOU TUDO! PARABENS, A palavra secreta era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreta:
        chances -= 1 #chances = chances - 1
    print(f'Você ainda tem {chances} chances. ')
    print()