from time import sleep
c = int(input('Qual o incio da contada? '))
f = int(input('Qual o fim da contagem? '))

for nome in range(c, f, -1):
	sleep(1)
	print(nome)
for ano in range(0,5):
    print('\033[1;32mFELIZ ANO NOVO!')