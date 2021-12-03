# quilo|hecto|deca|    |deci|cent|mili
#    Q.    H    da        dm   cm   mm
d = float(input('diga uma distância em metros: '))
c = d*100
m = d*1000
print('{} metros convertido em centímetros é {}cm!' .format(d, c), end=' ')
print('{} metros convertido em milímetros é {}mm'.format(d, m))