from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('Escolha uma opção!')
opção = 0
while opção != 5:
	print('''[ 1 ] Soma 	
[ 2 ] Multiplicação	
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do programa''')
	opção = int(input('Qual a sua opção'))
	if opção == 1:
		soma = n1 + n2
		print('A soma de {} e {} é {}'.format(n1, n2, soma))
	elif opção == 2:
		produto = n1 * n2
		print('O produto de {} e {} é {}'.format(n1, n2, produto))
	elif opção == 3:
		if  n1 > n2:
			maior = n1
		else:
			maior = n2
		print('O maior entre {} e {} é {}! '.format(n1, n2, maior))
	elif opção == 4:
		print('Informe os numeros novamente')
		n1 = int(input('Primeiro numero: '))
		n2 = int(input('Segundo numero: '))
	elif opção == 5:
		print('Finalizando...')
	else:
		print('Opção invalida! Tente novamente')
	print('=~='*10)




sleep(1)
print('fim do programa!')

	