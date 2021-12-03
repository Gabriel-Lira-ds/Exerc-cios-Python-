from datetime import date
ano_atual = date.today().year
nome = input('Nome:')
ano = int(input('Ano de nascimento: '))
idade = ano_atual-ano
if idade <= 9:
	print('''Nome: {}
Idade: {}
Categoria: Mirim'''.format(nome, idade))
elif idade <= 14:
	print('''Nome: {}
Idade: {}
Categoria: Infantil'''.format(nome, idade))
elif idade <= 19:
		print('''Nome: {}
Idade: {}
Categoria: Junior'''.format(nome, idade))
elif idade <= 24:
		print('''Nome: {}
Idade: {}
Categoria: Sênior'''.format(nome, idade))
else:
		print('''Nome: {}
Idade: {}
Categoria: Master'''.format(nome, idade))
	
	
	
	

