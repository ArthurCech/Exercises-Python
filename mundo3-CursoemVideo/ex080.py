# crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela

numbers = list()

for count in range(5):
    number = int(input(f'digite o {count + 1}º número inteiro: '))

    if count == 0 or number > numbers[-1]:
        numbers.append(number)
    else:
        ind = 0
        while ind < len(numbers):
            if number <= numbers[ind]:
                numbers.insert(ind, number)
                break
            ind += 1

print('Lista: ', end='')
for number in numbers:
    print(f'{number} ', end='')
