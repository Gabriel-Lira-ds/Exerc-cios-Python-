from datetime import date
ano_atual = date.today().year
ano = int(input('Qual o ano de nascimentio? '))
print(ano_atual)
idade = ano_atual-ano

# Maior de idade
Al = idade - 18
ano_d_alis = ano_atual-Al

# Menor de idade
Af = 18-idade
ano_d_alist = ano_atual+Af

print('Quem nascel em {} têm {} anos  em {}'.format(ano, idade, ano_atual))
if idade > 18:
	print('\033[1;31mVocê ja deveria ter se alistado há {} anos!'.format(Al))
	print('Seu a alistamento foi em {}\033[m!'.format(ano_d_alis))
elif idade < 18:
	print('Você ira se alistar daque a {} anos  em {}'.format(Af, ano_d_alist))
else:
	print('\033[1;32mVocê deve se alistar esse ano!')
	
	
