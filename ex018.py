import math
n = float(input('Degite um número: '))
print('{} arredondado pra cima fica {}!'.format(n, math.ceil(n)),end='! ')
print('{} arredondado pra baixo fica {}!'.format(n, math.floor(n)))
print('{} sem a parte decimal fica {}!'.format(n, math.trunc(n)))
print('{} elevado a 2 é {}!'.format(n, math.pow(n, 2)))
print('A raíz de quadrada de {} é {}! '.format(n, math.sqrt(n)))