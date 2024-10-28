from random import randint
from time import sleep
compudador = randint(0, 10) # "Faz o compudador pensar"
print('-=-' * 25)
print('Vou pensar em um número entre 0 e 9. Tente adivinhar...')
print('-=-' * 25)
jogador: int = int(input('Em que número eu pensei? ')) # "Jogador tenta adivinhar"
print('PROCESSANDO...')
sleep(3)
if jogador == compudador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(compudador, jogador))