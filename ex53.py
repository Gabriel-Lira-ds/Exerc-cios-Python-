frase = str(input('Degite uma frase: ')).upper().split()
junto = ''.join(frase)
#print(junto)
inverso = ('')
for letra in range(len(junto)-1, -1 ,-1):
	inverso = inverso+junto[letra]
if inverso == junto:
	print('Temos um palindromo')
else:
	print('A frase degitada não é  palindromo')
	
'''        outra opsão
rase = str(input('Digite uma frase: ')).upper().split()
junto = ''.join(frase)
inverso = junto[::-1]
if inverso == junto:
	print('Temos um palindromo')
else:
	print('A frase digitada não é um palindromo')'''
	