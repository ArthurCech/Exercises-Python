# Escreva um programa que leia três números reais e informe se eles constituem os 
# lados de um triângulo. Em caso afirmativo, informe se o triângulo é equilátero, 
# isósceles ou escaleno. Para que três números formem um triângulo deve ocorrer que 
# a soma dos dois lados menores deve ser maior que o lado maior. Para resolver essa 
# questão será preciso usar os operadores and e or.

ladoA = float(input('digite o valor do ladoA: '))
ladoB = float(input('digite o valor do ladoB: '))
ladoC = float(input('digite o valor do ladoC: '))

if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    if ladoA == ladoB and ladoA == ladoC:
        print('     triângulo equilátero ({} {} {})'.format(ladoA, ladoB, ladoC))
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print('     triângulo isósceles ({} {} {})'.format(ladoA, ladoB, ladoC))
    else:
        print('     triângulo escaleno ({} {} {})'.format(ladoA, ladoB, ladoC))
else:
    print('não é um triângulo ({} {} {})'.format(ladoA, ladoB, ladoC))
