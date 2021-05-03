# faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

sumNumbers = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        sumNumbers += i

print('Soma dos ímpares múltiplos de 3: {}'.format(sumNumbers))
