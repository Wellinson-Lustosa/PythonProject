print('\033[1;36m-=\033[m' * 33)
print('\033[4;34;45mAnalisador de Triângulos\033[m')
print('\033[1;36m-=\033[m' * 33)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima \033[1;35;42mPODEM FORMA\033[m triângulo!')
else:
    print('Os segmento acima \033[1;31;42mNÃO PODEM FORMA!\033[m')