salário = float(input('Qual é o salário. R$ = .'))
novo = salário + (salário * 20 / 100)
print('Um funcionário que ganhava R$ = {:.2f}, com 20% de aumento, passa a receber R$ = {:.2f}'. format(salário, novo))
