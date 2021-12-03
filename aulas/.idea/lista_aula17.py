# Para adicionar elementos na lista
lanches = ['suco', 'pudin', 'pizza']

# Usando o "append":
lanches.append('picoler')

# Usando o "insert"
lanches.insert(3, 'biscoito')

#Para remover itens da listas:

#EX:


print(lanches)

del lanches[0]

lanches.pop()

lanches.remove('pudin')

print(lanches)

lanches.append('sorvete')
if 'sorvete' in lanches:
    lanches.remove('sorvete')
else:
    print('lanche nao encontrado')



valores = list(range(4, 11))
print(valores)

valores2 = [5, 6, 1, 4, 10, 3, 0.1, 0.2]
# O '.sort()' colocar os valores em ordem crescente!
valores2.sort()
print(valores2)

# o '.sort(reverse=True)' colocar os valore em ordem decrescente!
valores2.sort(reverse=True)
print(valores)

# O 'len()' mostra o numero de valore na lista
print(len(valores2))

# Printar os inténs da lista sem as aspas e colcheites
nomes = ['Gabriel', 'José', 'Maria', 'Marta']
print(*nomes, sep= ', ')

# Mostrar os elementos das lista usando o 'for'!
for c, v in enumerate(valores):
    print(f'\033[1;33mNa posição {c} encontra-se o valor {v}')
print('Gheguei no final da lista!')

valores3 = list()
for cont in range(0, 5):
    va = int(input('Digite um valor:'))
    valores3.append(va)
print(valores3)

