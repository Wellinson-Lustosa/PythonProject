'''import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Teceiro aluno: '))
n4 = str(input('Quarto aluno: '))
liste = [n1, n2, n3, n4]
escolhar = random.choice(liste)
print('O aluno escolhido foi {}'.format(escolhar))'''
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Teceiro aluno: '))
n4 = str(input('Quarto aluno: '))
liste = [n1, n2, n3, n4]
escolhido = choice(liste)
print('O aluno escolhido foi {}'.format(escolhido))