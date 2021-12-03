km = float(input('Qual a distância da viagem? '))
print('Você está prete a fazer uma viagem de {}km!'.format(km))
if km >= 200:
    print('O valor da sua viagem vai ser de R${}'.format(km*0.45))
else:
    print('O valor da sua viagem vai ser de R${}'.format(km*0.50))
