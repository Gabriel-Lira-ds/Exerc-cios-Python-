a = float(input('Diga a altura da sua parede: '))
l = float(input('Diga a largura da sua parede: '))
área = a*l
print('A sua parede mede {}x{} e sua area é de {}m²!'.format(a, l, área), end=' ')
print('Para você pinta sua parede você precisa comprar {} litros de tinta!'.format(área/2))
