from random import randint
from time import sleep
sorteio = randint(0, 5)
print('=*='+' =*= '*8)
print('Adivinhe o número que irei pensa!') 
print('=*='+' =*= '*8)
escolha = int(input('Diga um número de 0 a 5: '))
print('processando...')
sleep(2)
if sorteio == escolha:
    print('Parabens você acertou!')
else:
    print('Você errou! Tente novamente!')


