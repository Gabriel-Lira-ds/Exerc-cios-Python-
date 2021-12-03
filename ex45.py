import random
from time import sleep
print('''Escolha a sua opção!
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] Tesoura''')
pe = 'Pedra'
pa = 'Papel'
te = 'Tessoura'
lista = [pe,  pa,  te]
escolhido = random.choice(lista)
print(escolhido)
jogada = int(input('Qual a sua jogada? '))
print('jo')
sleep(1)
print('Kem')
sleep(1)
print('pool')
sleep(1)
if jogada == 0:
	if escolhido == pe:
		print('O pc tambem escolheu PEDRA! Tente novamente!')
	if escolhido == pa:
		print('O pc escolheu PAPEL! Você perdeu!')
	elif escolhido == te:
		print('O pc escolheu TESOURA! Você ganhou')
elif jogada == 1:
	if escolhido == pe:
		print('O pc escolheu PEDRA! Você ganhou!')
	elif escolhido == pa:
		print('O pc também escolhei PAPEL! Tente novamente!')
	else:
		print('O pc escolheu TESOURA! Você perdeu!')
elif jogada == 2:
	if escolhido == pe:
		print('O pc escolheu PEDRA! Você gamhou!')
	elif escolhido == pa:
		print('O pc escolheu PAPEL! Você ganhou!')
	elif escolhido == te:
		print('O pc também escolheu TESSOURA! Tente novamente!')
if jogada > 2:
	print('\033[1;31mEssa jogada é invalida!\033[m')
	
