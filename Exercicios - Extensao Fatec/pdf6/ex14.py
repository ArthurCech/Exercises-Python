print('exercício 14')

list_a = []
for count in range(10):
    number = int(input('digite o {}º número inteiro para a lista A: '.format(count + 1)))
    list_a.append(number)

list_b = []
for count in range(10):
    number = int(input('digite o {}º número inteiro para a lista B: '.format(count + 1)))
    list_b.append(number)

final_list = list_a.copy()
final_list.extend(list_b)

print('Lista final (junção de A com B): {}'.format(final_list))

print('fim do programa')
