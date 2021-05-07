print('exercício 15')

length_a = int(input('digite o tamanho da lista A: '))

while length_a <= 0:
    length_a = int(input('[ERRO] digite o tamanho da lista A: '))

length_b = int(input('digite o tamanho da lista B: '))

while length_b <= 0:
    length_b = int(input('[ERRO] digite o tamanho da lista B: '))

list_a = []
for count in range(length_a):
    number = int(input('digite o {}º número inteiro para a lista A: '.format(count + 1)))
    list_a.append(number)

list_b = []
for count in range(length_b):
    number = int(input('digite o {}º número inteiro para a lista B: '.format(count + 1)))
    list_b.append(number)

final_list = list_a.copy()
final_list.extend(list_b)

print('Lista final (junção de A com B): {}'.format(final_list))

print('fim do programa')
