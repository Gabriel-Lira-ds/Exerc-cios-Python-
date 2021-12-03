preço = float(input('Valor do produto: R$'))
print('''[ 1 ] Avista no dinheiro/cheque
[ 2 ] Avista cartão de débito
[ 3 ] 2x no cartão de crédito
[ 4 ] 3x ou mais com 20% juros no cartão da crédito''')
pag= int(input('Qual a opção? '))
if pag == 1:
	des = preço*0.90
	print('Avista no dinheiro/cheque o produto ganhara 10% de desconto!De R${} custará R${}!'.format(preço, des))
elif pag==2:
	des = preço*0.95
	print('Avista no cartão/debito o produto ganhara 5% de desconto!De R${} custará R${}!'.format(preço, des))    
elif pag==3:
	des = preço/2
	print('Duas vezes no cartão a parcela ficará {:.2f}'.format(des))
elif pag==4:
	des = preço**1.20
	quantidade = int(input('Quantas vezes? '))
	parc = des = quantidade
	print('{} vezes no cartão a parcela ficará {:.2f}'.format(quantidade, parc))
	
