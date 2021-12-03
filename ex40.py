'''média igual oua baixo de 5 Reprovado
   media entre 5 e 6,5 Recuperação
   média igual ou acima de 7 Aprovado'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('Tirando {} e {}! A média ficará {}!'.format(n1, n2, media))
if media <= 5:
    print('\033[1;31mO aluno está Reprovado!\033[m')
if media > 5 and media <= 6.5:
    print('O aluno está de Recuperação!')
elif media  >= 7:
    print('\033[1;32mO aluno está aprovado!\033[m')