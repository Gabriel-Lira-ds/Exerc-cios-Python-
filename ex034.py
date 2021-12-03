salário = float(input('Qual o salário do funcionário? R$'))
if salário > 2250:
    p = salário*1.15
else:
    p = salário*1.5
print('O salário do funcionário sera reajustado para \033[7;31;46mR${}\033[m'.format(p))
