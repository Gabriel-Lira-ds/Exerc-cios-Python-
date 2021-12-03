primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
a = primeiro+(10-1 )* razão                           
# [ formula da  PA ]   an = a1 + (n – 1)r
for c in range(primeiro, a, razão):
	print('{}'.format(c),end='-')
print('acabou!')
