print('Exercício 04 do PDF Parte 3')

n = int(input('Digite a quantidade de elementos: '))

i = 0
somaPositivo = 0
while i < n:
    num = float(input('Digite um número real: '))
    if num > 0:
        somaPositivo += num

print('Soma dos valores reais positivos = {}'.format(soma))

print('Fim do programa')