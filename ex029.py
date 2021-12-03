velocidade = float(input('Qual a velocidade do carro? '))
if velocidade>=80:
    print('\033[1;31mVocê excedeu a velocidade!A sua multa é de R${}\033[m'.format((velocidade - 80)*7))

else:
    print('\033[1;32mVocê está dentro da velocidade permitida\033[m')
print('Dirija com cuidado')   
