print('exercício 6')

name = input('digite o nome do lutador: ')
weight = float(input('digite o peso do lutador: '))

if weight < 65:
    category = 'Pena'
elif weight < 72:
    category = 'Leve'
elif weight < 79:
    category = 'Ligeiro'
elif weight < 86:
    category = 'Meio médio'
elif weight < 93:
    category = 'Médio'
elif weight < 100:
    category = 'Meio pesado'
else:
    category = 'Pesado'

message = 'O lutador {} pesa {:.1f} kg e se enquadra na categoria {}'
print(message.format(name, weight, category))

print('fim do programa')
