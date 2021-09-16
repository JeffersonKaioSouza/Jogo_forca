'''
Jogo da forca
'''

secreto = 'perfume'
digitadas = []
chances = 5
print('=' * 20)
print('Usado por homens e mulheres, existem caros e baratos,\n'
      'alguns são doces outros nem tanto, alguns são cheirosos outros não!!\n'
      'Sabe oque é ?')
print('=' * 20)

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ').strip().lower()

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AAHHH,a letra "{letra}" Não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal você ganhou!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')