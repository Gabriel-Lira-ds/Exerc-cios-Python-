print('-=-'*10)
print('        Gerado de PA')
print('-=-'*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
	total = total + mais
	while cont != total:
		print('{}'.format(termo),end='-')
		termo += razão
		cont += 1
	print('Pausa')
	mais = int(input('\nQuantos voçê quer a mais: '))
print('Fim!!!')
print(total)

