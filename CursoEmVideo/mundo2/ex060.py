# faça um programa que leia um número qualquer e mostre o seu fatorial

number = int(input('digite o número que deseja saber o fatorial: '))

i = number
fat = 1
while i > 0:
    fat *= i
    i -= 1

print('{}! = {}'.format(number, fat))
