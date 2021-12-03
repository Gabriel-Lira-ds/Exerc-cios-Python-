n1 = float(input('Seguimento 1: '))
n2 = float(input('Seguimento 2: '))
n3 = float(input('Seguimento 3: '))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
	print('Esses seguimento podem forma triangulo', end=' ')
	if  n1 == n2 ==n3:
		print('Equilatero')
	elif n1 != n2 != n3:
		print('Escaleno')
	else:
		print('isóscele')
else:
	print('Esses seguimetos não pode formar triangulo ')
