frase = str(input('Diga uma frase: ')).strip().upper()
print('A frase possui {} letras A'.format(frase.count('A')))
print('A primeira letra "A" está na posição {}'.format(frase.find('A')+1))