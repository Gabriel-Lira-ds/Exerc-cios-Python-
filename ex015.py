d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro percorreu? '))
v = (d*60)+(km*0.15)
print('O cliente irá pagar R${}'.format(v))