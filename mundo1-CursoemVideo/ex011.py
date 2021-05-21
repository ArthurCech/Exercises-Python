# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

width = float(input('digite a largura da parede: '))
height = float(input('digite a altura da parede: '))

area = width * height
qtd_ink = area / 2

print('Área da parede: {:.2f}m²'.format(area))
print('Quantidade de tinta: {:.2f} litro(s)'.format(qtd_ink))
