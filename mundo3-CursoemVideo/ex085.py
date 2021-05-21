# crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

numbers = [[], []]

for count in range(7):
    number = int(input(f'digite o {count + 1}º número inteiro: '))

    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)

numbers[0].sort()
numbers[1].sort()

print(f'Valores pares digitados: {numbers[0]}')
print(f'Valores ímpares digitados: {numbers[1]}')
