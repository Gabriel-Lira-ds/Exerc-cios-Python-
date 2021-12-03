sexo = str(input('Informe seu sexo:[ M / F ] ')).strip()
while sexo not in 'MmFf':
	sexo = str(input('Opcão invalida! Por favor, Tente novamente! [ M / F ]')).strip()
print('Sexo {} registrado com sucesso! '.format(sexo))