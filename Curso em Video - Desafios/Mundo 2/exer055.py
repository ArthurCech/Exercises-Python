# faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o 
# maior e o menor peso lidos.

for i in range(5):
    weight = float(input('digite o peso da pessoa {}: '.format(i + 1)))

    if i == 0:
        bigger = smaller = weight
    elif weight > bigger:
        bigger = weight
    elif weight < smaller:
        smaller = weight

print('Maior peso inserido: {}'.format(bigger))
print('Menor peso inserido: {}'.format(smaller))
