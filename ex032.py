ano = int(input('Diga um ano! Para saber se ele é bixesto!   '))
if (ano%4)==0 and ano%100!=0 or ano%400==0:
    print ('{} é bixesto!'.format(ano))
else:
    print('%i não é bixesto!'%(ano))
