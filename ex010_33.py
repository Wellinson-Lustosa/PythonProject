a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando quem é o menor número.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o maior número.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))