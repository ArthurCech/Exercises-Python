# faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    number = int(input('digite o número que deseja saber a tabuada: '))
    print('-' * 15)

    if number <= 0:
        break
    for i in range(1, 11):
        print(f'{number} x {i} = {number * i}')
    print('-' * 15)
