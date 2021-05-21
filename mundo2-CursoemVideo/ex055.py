# faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for count in range(5):
    weight = float(input('digite o peso da {}ª pessoa: '.format(count + 1)))

    if count == 0:
        biggest_weight = smallest_weight = weight
    elif weight > biggest_weight:
        biggest_weight = weight
    elif weight < smallest_weight:
        smallest_weight = weight

print('Maior peso lido: {} kg'.format(biggest_weight))
print('Menor peso lido: {} kg'.format(smallest_weight))
