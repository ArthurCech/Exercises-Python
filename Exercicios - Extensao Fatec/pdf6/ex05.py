print('exercício 5')

quantity = int(input('digite a quantidade de elementos (entre 1 e 50): '))

while quantity <= 0 or quantity > 50:
    quantity = int(input('[ERRO] digite a quantidade de elementos (entre 1 e 50): '))

list_numbers = []
list_neg = []
list_pos = []

for count in range(quantity):
    number = float(input('digite o {}º número real: '.format(count + 1)))
    list_numbers.append(number)

    if number >= 0:
        list_pos.append(number)
    else:
        list_neg.append(number)

print('Qtd. de elementos da lista de positivos = {}'.format(len(list_pos)))

print('Lista positivos:')
for number in list_pos:
    print(number)
    
print('Qtd. de elementos da lista de negativos = {}'.format(len(list_neg)))

print('Lista negativos:')
for number in list_neg:
    print(number)

print('fim do programa')
