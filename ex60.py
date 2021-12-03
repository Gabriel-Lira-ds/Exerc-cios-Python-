from math import factorial
n = int(input('Degite um numero para saber seu factorial: '))
c = n
while c > 0:
	print('{}! = {}'.format(n, c),end=' ')
	print('x ' if c > 1 else '=', end='')
	c -= 1
	
