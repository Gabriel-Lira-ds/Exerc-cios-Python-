from datetime import date
atual = date.today().year
contador = 0
contador1 = 0
for pessoa in range(1,8):
	ano = int(input('Em que ano a {}° pessoa nasceu: '.format(pessoa)))
	idade = atual-ano
	if idade<18:
		contador += 1
	else:
		contador1 += 1
if contador ==1:
	print('Ao todo tivemos {} pessoa menor de idade!'.format(contador))
elif contador>1:
	print('Ao todo tivemos {} pessoas menores  de idade!'.format(contador))
else:
	print('Não há menor de idade!')
#/////////////////////////////////////'
if contador1==1:
	print('E também tivemos {} pessoa maior de idade!'.format(contador1))
elif contador1>1:
	print('E também tivemos {} pessoas maiores de idade!'.format(contador1))	
else:
	print('Nao há menor de idade!')
	
			
	