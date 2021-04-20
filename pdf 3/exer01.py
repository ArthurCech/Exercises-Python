# Escreva um programa que calcule os N primeiros termos de uma progressão 
# geométrica (PG) com razão R e primeiro termo P fornecidos pelo usuário. 
# Também deve ser calculada e apresentada a soma desses N termos. Caso 
# de teste:
# Entrada: N = 8 P = 2 e R = 3
# Saída: 2 6 18 54 162 486 1458 4374

P = int(input('digite o primeiro termo: '))
R = int(input('digite a razão: '))
N = int(input('digite a quantidade de elementos que deseja visualizar: '))

i = 0
while i < N:
    print(P, end=' ')
    P = P * R
    i += 1
