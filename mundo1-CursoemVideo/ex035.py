# desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

side_a = float(input('digite o comprimento do lado A: '))
side_b = float(input('digite o comprimento do lado B: '))
side_c = float(input('digite o comprimento do lado C: '))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print('Os lados {} - {} - {} formam um triângulo'.format(side_a, side_b, side_c))
else:
    print('Os lados {} - {} - {} não formam um triângulo'.format(side_a, side_b, side_c))
