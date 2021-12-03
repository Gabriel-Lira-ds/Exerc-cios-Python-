#Diciplina: Introdução à Programação Estruturada
#Professor: José Patrício
#Aluno: Gabriel Lira dos Santos

list_pokém = []

while True:
    print('\033[1m-=\033[m' * 20)
    print('\033[1mEscolha uma opção!\033[m\n[ 1 ]Adicionar pokémom\n[ 2 ]Remover pokémom\n[ 3 ]Listar pokémons\n[ 4 ]Mostrar '
          'pokémom por letra incial\n[ 5 ]Sair')
    print('\033[1m-=\033[m' * 20)
    op = int(input('\033[1mDigite uma opção:\033[m '))

    if op == 1:
        adicionar = input('Digite o nome do pokémom: ').strip()
        if adicionar in list_pokém:
            print('\033[1;31mEsse Pokémom já está lista!\033[1m')
        else:
            list_pokém.append(adicionar)
            print('\033[1;32mPokémom adicionado na lista!\033[m')
    if op == 2:
        remover = input('Digite o nome do pokémom que serar removido: ').strip()
        if remover in list_pokém:
            list_pokém.remove(remover)
            print('\033[1;32mPokémom removido da lista!\033[m')
        else:
            print('Pokémom nao encontrado')
    if op == 3:
        print(*list_pokém, sep= ', ')

    if op == 4:
        letra = str(input('Digite a letra inicial: ')).strip()
        letra_inicial = []
        for l in list_pokém:
            if l.upper()[:1] == letra.upper()[:1]:
                letra_inicial.append(str(l))

        print(*letra_inicial, sep= ', ')

    if op > 5:
        print('\033[1;31mOpção invalida!\033[m')

    if op == 5:
        print('Saindo...')
        break
