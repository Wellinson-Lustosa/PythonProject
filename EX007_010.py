real = float(input('Quanto dinheiro tem na milha carteira. R$ '))
dolar = real / 5.46
euro = real / 5.91
print('Com R$ = {:.2f} você pode comprar US$ = {:.2f}'.format(real, dolar))
print('Com R$ = {:.2f} você pode comprar EUR$ = {:.2f}'.format(real, euro))
