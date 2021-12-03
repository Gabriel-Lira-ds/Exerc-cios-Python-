'''nome = input('Qual o seu nome?')
ano = int(input('Qual o ano do seu nacimento?'))
idade = 2021 - ano

if idade > 18:
    print('Você têm {} anos e é maior de idade!'.format(idade))

else:
    print(f'Olá {nome} vocé têm {idade} e ainda é menor de idade!')'''
import turtle

squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("blue")

for i in range(4000):
    squary.forward(i)
    squary.left(91)
