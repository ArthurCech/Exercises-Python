# faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo

number = int(input('digite o número que deseja saber a tabuada: '))

while number > 0:
    for count in range(1, 11):
        print('{} x {:2} = {:2}'.format(number, count, number * count))
        
    print('-' * 30)

    number = int(input('digite o número que deseja saber a tabuada: '))




# MÉTODO 2
while True:
    number = int(input('digite o número que deseja saber a tabuada: '))

    print('-' * 30)

    if number <= 0:
        break

    for count in range(1, 11):
        print(f'{number} x {count:2} = {number * count:2}')

    print('-' * 30)
