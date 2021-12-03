n = int(input('diga um número de 1 a 9999: ').strip())
u = n//1%10
d = n//10%10
c = n//100%10
m = n//1000%10
print('A unidade de {} é {}!'.format(n, u))
print('A desena de {} é {}!'.format(n, d))
print('A centena de {} é {}!'.format(n, c))
print('A milhar de {} é {}!'.format(n, m))
