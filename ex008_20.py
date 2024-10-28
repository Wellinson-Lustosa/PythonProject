'''import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
listes = [n1, n2, n3, n4]
random.shuffle(listes)
print('A ordem de apresentação será.')
print(listes)'''

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
liste = [n1, n2, n3, n4]
shuffle(liste)
print('A ordem de apresentação será')
print(liste)