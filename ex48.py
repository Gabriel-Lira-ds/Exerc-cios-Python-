soma = 0 # ira somar todos os numeros imapares impares
contador = 0 # ira contar quantos numeros impares
for impar in range(1, 501, 2):
	if impar%3==0:
		soma = soma+impar
		contador = contador+1
print('\033[1;36mA soma de todos os {} numeros imapares é {}\033[m'.format(contador, soma))