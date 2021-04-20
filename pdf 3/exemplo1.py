P = int(input('digite o primeiro termo: '))
R = int(input('digite a razão: '))
Q = int(input('digite a quantidade de elementos que deseja mostrar: '))

cont = 0
soma = 0
while cont < Q:
    print('Termo {} da PA = {}'.format(cont + 1, P))
    soma = soma + P
    P = P + R
    cont = cont + 1

print('somatória dos termos = {}'.format(soma))
