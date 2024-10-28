distância = float(input('Qual é a distâcia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
'''if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45'''

print('É o preço da sua passegem será de R${:.2f}.'.format(preço))
