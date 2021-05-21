# refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: equilátero - todos os lados iguais; isósceles - dois lados iguais; escaleno - todos os lados diferentes

side_a = float(input('digite o comprimento do lado A: '))
side_b = float(input('digite o comprimento do lado B: '))
side_c = float(input('digite o comprimento do lado C: '))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print('Os lados {} - {} - {} formam um triângulo '.format(side_a, side_b, side_c), end = '')
    
    if side_a == side_b == side_c:
        print('equilátero')
    elif side_a != side_b != side_c:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Os lados {} - {} - {} não formam um triângulo'.format(side_a, side_b, side_c))
