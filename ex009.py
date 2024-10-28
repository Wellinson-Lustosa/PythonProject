frase = ('Curso em Video Python '
         'Só você poderia nos salvar '
         'De uma escuridão que está a nos tomar. '
         'Pouco a pouco sinto que estou lembrando '
         'Os motivos para ter tanto medo.'
         'Tomando por completo a minha mente' 
         'Pensamentos misturados às vívidas passagens' 
         'De um livro sendo pouco a pouco lido' 
         'A nossa história está a se revelar')
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('Oi')
print("""Só você poderia nos salvar 
De uma escuridão que está a nos tomar. 
Pouco a pouco sinto que estou lembrando 
Os motivos para ter tanto medo.
Tomando por completo a minha mente 
Pensamentos misturados às vívidas passagens 
De um livro sendo pouco a pouco lido 
A nossa história está a se revelar """)
print(frase.count('o'))
print(frase.upper().count('o'))
print(len(frase.strip()))
print(frase.replace('Python', 'Luadeo'))

print('Curso' in frase)

print(frase.find('Curso'))

print(frase.find('Video'))

print(frase.find('video'))


print(frase.lower().find('video'))

print(frase.split())

dividido = frase.split()

print(dividido[2][3])