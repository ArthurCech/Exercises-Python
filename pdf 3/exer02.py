# Escreva um programa que leia valores numéricos inteiros e totalize 
# (totalizar é somar todos os números) separadamente os positivos e os 
# negativos até que o usuário digite 0. Ao final mostre na tela esses 
# dois totais. Caso de teste:
# Entrada: 12 -3 5 1 -4 -9 6 0
# Saída: 
# Total dos positivos = 24
# Total dos negativos = -16

somaPositivos = 0
somaNegativos = 0
X = 1
while X != 0:
    X = int(input('digite o valor: '))
    if X >= 0:
        somaPositivos += X
    else:
        somaNegativos += X

print('Total dos positivos = {}'.format(somaPositivos))
print('Total dos negativos = {}'.format(somaNegativos))
