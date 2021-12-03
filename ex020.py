import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segurado aluno: '))
n3 = str(input('nome do terceiro aluno: '))
n4 = str(input('nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido foi {}!'.format(escolhido))