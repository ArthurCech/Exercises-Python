# faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

def area(width, length):
    area = width * length
    print(f'Área do terreno ({width}x{length}): {area} m²')


width = int(input('digite a largura do terreno em metros: '))
length = int(input('digite o comprimento do terreno em metros: '))

area(width, length)
