peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m)'))
calculo = peso / (altura**2)
print('\033[1;32mIMC = {:.2f}'.format(calculo))
if calculo <= 18.5:
	print('Você abaixo do pesso ideal')
elif calculo > 18.5 and calculo < 25:
	print('Seu IMC está normal!')
elif calculo >= 25 and calculo < 30:
	print('Você está com sobrepeso!')
elif calculo >= 30 and calculo < 40:
	print('Você está obesa!')
else:
	print('Você está com obessidade morbita!')
	