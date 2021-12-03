from math import radians, sin, cos, tan
ângulo = float(input('Degite um ângulo: '))
seno = sin(radians(ângulo))
print('O seno de {}° é {:.2f}!'.format(ângulo, seno))
coseno = cos(radians(ângulo))
print('O coseno de {}° é {:.2f}!'.format(ângulo, coseno))
tangente = tan(radians(ângulo))
print('A tangente de {} é {:.2f}'.format(ângulo, tangente))