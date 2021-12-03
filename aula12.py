'''nome = str(input('Qual o seu nome? ')).capitalize().split()
if nome == 'Gabriel':
    print('Seu nome é muito bonito! {}.'.format(nome))
elif nome == 'Pedro' or nome == 'Paulo' or nome == 'Rodrigo':
    print('Seu nome é bem popular entre os homens no Brasil! {}.'.format(nome))
elif nome == 'Maria' or nome == 'Clara' or nome == 'Ana':
    print('Seu nome e bem popular entre as mulheres no Brasil! {}.'.format(nome))'''

velocidade = float(input("Qual a velocidade do veiculo: "))

if velocidade > 80:
    veloUltramadada = velocidade - 80
    multa = veloUltramadada * 5
    print('O veiculo utrapassou {} km da velocidade permitida e foi multado em R${}.'.format(veloUltramadada, multa))
else:
    print('Veiculo dentro da velocidade permitda!')