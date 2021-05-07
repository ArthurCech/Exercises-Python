print('exercício 2')

number = int(input('digite um número inteiro: '))

sum_positive = sum_negative = 0

while number != 0:
    if number > 0:
        sum_positive += number
    else:
        sum_negative += number  
         
    number = int(input('digite um número inteiro: '))

print('Total dos positivos = {}'.format(sum_positive))
print('Total dos negativos = {}'.format(sum_negative))

print('fim do programa')
