# desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

sideA = float(input('digite o comprimento do lado A: '))
sideB = float(input('digite o comprimento do lado B: '))
sideC = float(input('digite o comprimento do lado C: '))

if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA:
    print('\033[1;32mOs lados \033[1;35m(A: {} - B: {} - C: {}) \033[1;32mformam um triângulo\033[m'.format(sideA, sideB, sideC))
else:
    print('\033[1;31mOs lados \033[1;35m(A: {} - B: {} - C: {}) \033[1;31mnão formam um triângulo\033[m'.format(sideA, sideB, sideC))
