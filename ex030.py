num = int(input('Diga um valor qualquer: '))
if (num/2) == int(num/2):
    print('%i é um número PÁR'%(num))
else:
    print('%i é um número IMPAR'%(num))

#  /////outra opção/////
num = int(input('Diga um valor qualquer: '))
if (num%2) == 0:
    print('{} é um número PÁR'.format(num))
else:
    print('{} é um número IMPAR'.format(num))

