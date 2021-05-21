# crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for number in range(1, 51):
    if number % 2 == 0:
        print('{} '.format(number), end = '')
        
print('fim do programa')
