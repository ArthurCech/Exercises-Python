# desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

sum_numbers = 0

for count in range(6):
    number = int(input('digite um número inteiro: '))

    if number % 2 == 0:
        sum_numbers += number

print('Soma dos números pares: {}'.format(sum_numbers))
