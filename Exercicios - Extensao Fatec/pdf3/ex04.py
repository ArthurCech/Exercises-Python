print('exercício 4')

quantity = int(input('digite a quantidade de número reais: '))

count = sum_positive = 0

while count < quantity:
    number = float(input('digite um número real: '))

    if number > 0:
        sum_positive += number
        
    count += 1

print('Soma dos valores positivos digitados = {}'.format(sum_positive))

print('fim do programa')
