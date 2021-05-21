# faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior

from random import randint


def generate_numbers(numbers):
    for count in range(5):
        number = randint(1, 10)
        numbers.append(number)
        print(f'{number} ', end='', flush=True)
    print('\nlista preenchida!')


def sum_even(numbers):
    sum_numbers = 0

    for value in numbers:
        if value % 2 == 0:
            sum_numbers += value
    
    print(f'Soma dos valores pares = {sum_numbers}')


numbers = list()
generate_numbers(numbers)
sum_even(numbers)
