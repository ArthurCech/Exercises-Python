# refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de 
# triângulo será formado:
# equilátero: todos os lados iguais
# isósceles: dois lados iguais
# escaleno: todos os laods diferentes

sideA = float(input('digite o valor do lado A: '))
sideB = float(input('digite o valor do lado B: '))
sideC = float(input('digite o valor do lado C: '))

if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA:
    print('Os lados ({} | {} | {}) formam um triângulo'.format(sideA, sideB, sideC), end='')

    if sideA == sideB == sideC:
        print(' equilátero')
    elif sideA == sideB or sideA == sideC or sideB == sideC:
        print(' isósceles')
    else:
        print(' escaleno')
else:
    print('Os lados ({} | {} | {}) não formam um triângulo'.format(sideA, sideB, sideC))
