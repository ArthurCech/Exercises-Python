# refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: equilátero, isósceles ou escaleno

sideA = float(input('digite o comprimento do lado A: '))
sideB = float(input('digite o comprimento do lado B: '))
sideC = float(input('digite o comprimento do lado C: '))

if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA:
    print('Os lados (A: {} - B: {} - C: {}) formam um triângulo'.format(sideA, sideB, sideC), end=' ')
    
    if sideA == sideB == sideC:
        print('EQUILÁTERO')
    elif sideA == sideB or sideA == sideC or sideB == sideC:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os lados (A: {} - B: {} - C: {}) não formam um triângulo'.format(sideA, sideB, sideC))
