somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
	print('{}{}° Pessoa{}'.format((7*'-'), p, (7*'-')))
	nome = str(input('Nome: ')).strip()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo  [M/F]: '))
	somaidade += idade
	if p == 1 and sexo in 'Mm':
		maioridadehomem = idade
		nomevelho = nome
	if sexo in 'Mm' and idade > maioridadehomem:
		maioridadehomem = idade
		nomevelho = nome
	if sexo in 'Ff' and idade < 20:
		totmulher += 1

media = somaidade/4
print('A media de idade do grupo é {} anos!'.format(media))
print('O homem mais velho se chama {} e têm {} anos'.format(nomevelho, maioridadehomem))
print('Existe {} mulheres com menos de 20 anos'.format(totmulher))
	
