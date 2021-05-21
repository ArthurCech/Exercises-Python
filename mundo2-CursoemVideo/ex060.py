# faça um programa que leia um número qualquer e mostre o seu fatorial

number = int(input('digite o número que deseja saber o fatorial: '))

print('{}! = '.format(number), end = ' ')

fat = 1
count = number

while count > 0:
    print('{}'.format(count), end = '')
    print(' x ' if count > 1 else ' = ', end = '')
    fat *= count
    count -= 1
print('{}'.format(fat))
