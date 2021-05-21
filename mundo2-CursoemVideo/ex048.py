# faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

sum_numbers = 0

for number in range(1, 501):
    if number % 2 != 0 and number % 3 == 0:
        sum_numbers += number
    
print('Soma dos números ímpares múltiplos de 3 que estão entre 1 e 500: {}'.format(sum_numbers))
