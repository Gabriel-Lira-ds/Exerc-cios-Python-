num = int(input('Diga um numero: '))



while True:
	print('''Escolha a opção que você quer converter!
	[ 1 ] Binário!
	[ 2 ] octal!
	[ 3 ] hexadecimal!''')
	op = int(input('Qual a sua opicao? '))
	if op == 1:
		print('O {} convertido pra binario é \033[1;36m {} \033[m !' .format(num, bin(num)[2:]))
	elif op == 2:
		print('O {} convertido pra octal é \033[1;36m {} \033[m'.format(num, oct(num)[2:]))
	elif op == 3:
		print('O {} convertido pra hexadecimal é \033[1;36m {} \033[m!'.format(num, hex(num)[2:]))

	escolha = input('Quer continuar? [\033[1;33m SIM \033[m / \033[1;31m NÃO \033[m}: ').upper()
	if escolha[0] == 'N':
		break
	else:
		num = int(input('Diga um numero: '))
	

