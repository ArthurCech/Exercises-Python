# crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) quantos números foram digitados; B) a lista de valores ordenada de forma decrescente; C) se o valor 5 foi digitado e está ou não na lista

numbers = list()

while True:
    numbers.append(int(input('digite um número inteiro: ')))

    enter_number = input('digitar mais um número [S/N]: ').strip().upper()[0]

    if enter_number == 'N':
        break

print(f'Quantidade de números digitados: {len(numbers)}')
numbers.sort(reverse=True)
print(f'Lista de valores ordenada de forma decrescente: {numbers}')
print('O valor 5 está na lista' if 5 in numbers else 'O valor 5 não está na lista')
