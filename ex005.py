n1 = int(input ('digite um número: '))
n2 = int(input('digire out número: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
print('A soma vale {}, \n a multiplicação vale {}, e a divisão é {:.3f}!'.format(s, m, d), end = '')
print('A divisão inteira vale {}, e a potência vale {}!'.format(di, p))