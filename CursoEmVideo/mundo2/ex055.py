# faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for i in range(5):
    weight = float(input('digite o peso da {}ª pessoa: '.format(i + 1)))

    if i == 0:
        biggest = smallest = weight
    elif weight < smallest:
        smallest = weight
    elif weight > biggest:
        biggest = weight

print('Maior peso lido: {:.2f}'.format(biggest))
print('Menor peso lido: {:.2f}'.format(smallest))
