from random import randint
computador = randint(1, 10)
print('\033[1;36mSou seu computador...Vou pensar em um nemero!\033[m] \n\033[1;32mSera que você consegue adivihar qual foi?\033[m')
acertou = False
palpite = 0
while not acertou:
	jogador = int(input('\033[1;33mQual o seu palpite?\033[m] '))
	palpite += 1
	if jogador == computador:
		acertou = True
	else:
		if computador > jogador:
			print('\033[1;36mMais...Tente novamente!\033[m')
		elif computador < jogador:
			print('\033[1;32mMenos... Tente novamente!\033[m')
				
print('\033[1;31mAcertou! Com {} tentativas !\033[m'.format(palpite))