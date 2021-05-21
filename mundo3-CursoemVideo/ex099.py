# faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual delas é o maior

def maior(list_numbers):
    count = 0

    for value in list_numbers:
        print(f'{value} ', end='', flush=True)
        print()

        if count == 0:
            biggest = value
        elif value > biggest:
            biggest = value

        count += 1
    
    print(f'Qtd. de valores digitados: {count}')
    print(f'Maior valor informado: {biggest}')


numbers = list()

while True: # conjunto de números

    while True: # números
        numbers.append(int(input('digite o número que deseja inserir: ')))

        while True:
            enter_number = input('digitar mais uma número [S/N]: ').strip().upper()[0]
            
            if enter_number in 'SN':
                break

        if enter_number == 'N':
            break

    maior(numbers)

    while True:
        again = input('digitar mais um conjunto de números [S/N]: ').strip().upper()[0]
            
        if again in 'SN':
            break

    numbers.clear()

    if again == 'N':
        break
