v = float(input('Diga o preço de um produto: R$'))
p  = float(input('diga quantos porcento de desconto você deseja:'))
d = v-v*(p/100)
print('O produto que custa R${}! Com {}% de desconto ira custar R${}'.format(v, p, d))