soma = 0
contador = 0
for n in range(1, 7):
	num = int(input('Digite o valor {}: '.format(n)))
	if num % 2 == 0:
		soma = soma+num
		contador = contador+1
		
print('Você degitou {} PARES! E a soma entre eles é{}'.format(contador, soma))