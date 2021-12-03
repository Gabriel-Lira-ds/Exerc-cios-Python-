co = float(input('diga o valor do cateto oposto: '))
ca = float(input('Diga o valor do cateto adjacente: '))
h = (co**2 + ca**2)**(1/2)
print('\033[1;32mA hipótenusa vale {:.2f}'.format(h))
