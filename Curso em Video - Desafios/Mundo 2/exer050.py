# desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
# pares. Se o valor digitado for ímpar, desconsidere-o

sumEvenNumbers = 0
for i in range(6):
    number = int(input('digite um número inteiro: '))
    if number % 2 == 0:
        sumEvenNumbers += number
    
print('Soma dos valores pares: {}'.format(sumEvenNumbers))
