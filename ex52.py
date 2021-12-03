num = int(input('Degite um numero: '))
total = 0
for c in range(1, num + 1):
	if num % c ==0:
		print('\033[1;32m',end=' ' )
		total += 1 # ou total = total + 1
	else:
		print('\033[1;31m',end=' ')
	print('{}'.format(c),end=' ')
print('\n\033[m{} foi divisivel por {} numeros!'.format(num, total))
if total ==2:
	print('\033[4;36mPortanto ele é primo!')
else:
	print('Portanto não é primo')


	