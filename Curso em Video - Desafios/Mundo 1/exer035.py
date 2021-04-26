# desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas 
# podem ou não formar um triângulo

ladoA = float(input('digite o valor do ladoA: '))
ladoB = float(input('digite o valor do ladoB: '))
ladoC = float(input('digite o valor do ladoC: '))

if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print('\033[1;32mÉ um triângulo ({} | {} | {})\033[m'.format(ladoA, ladoB, ladoC))
else:
    print('\033[1;31mNão é um triângulo ({} | {} | {})\033[m'.format(ladoA, ladoB, ladoC))
