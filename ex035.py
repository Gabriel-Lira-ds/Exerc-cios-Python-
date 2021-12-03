print (('-=')*21)
print('             Digite três valor')
print (('-=')*21)

n1 = float(input('Primeiro seguimento: '))
n2 = float(input('Segundo seguimento: '))
n3 = float(input('Terceiro seguimento: '))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n2+n1:
    print ('\033[1;31;42mEsses seguimento podem forma um triângulo!\033[m')
else:
    print ('\033[1;32;41mEsses seguimento não pode formar um tringulo\033[m]')
