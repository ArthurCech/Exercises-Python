# faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

height = float(input('digite a altura da parede: '))
width = float(input('digite a largura da parede: '))

area = height * width
ink = area / 2

print('\033[1;33mPara pintar {}m² será(ão) necessário(s) \033[1;31m{} litro(s) de tinta\033[m'.format(area, ink))
