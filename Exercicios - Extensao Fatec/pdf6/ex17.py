print('exercício 17')

length_a = int(input('digite o tamanho da lista A: '))

while length_a <= 0:
    length_a = int(input('[ERRO] digite o tamanho da lista A: '))

length_b = int(input('digite o tamanho da lista B: '))

while length_b <= 0:
    length_b = int(input('[ERRO] digite o tamanho da lista B: '))

list_a = []
for count in range(length_a):
    number = int(input('digite o {}º número inteiro para lista A: '.format(count + 1)))
    while number in list_a:
        number = int(input('[ERRO] digite o {}º número inteiro para lista A: '.format(count + 1)))
    list_a.append(number)

list_b = []
for count in range(length_b):
    number = int(input('digite o {}º número inteiro para lista B: '.format(count + 1)))
    while number in list_b:
        number = int(input('[ERRO] digite o {}º número inteiro para lista B: '.format(count + 1)))
    list_b.append(number)

final_list = list_a.copy()

for i in range(len(list_b)):
    if list_b[i] not in final_list:
        final_list.append(list_b[i])

print('Lista gerada: {}'.format(final_list))

print('fim do programa')
