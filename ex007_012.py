preço = float(input('Qual é o preço do produto. R$ = '))
novo = preço - (preço * 5 / 100)
print('O produto que custava R$ = {:.2f}, na promoção com 5% vai custaR$ = {:.2f}.'.format(preço, novo))
