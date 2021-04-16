print('Exercício 06 do PDF Parte 2')

nome = input('Digite o nome do lutador: ')
peso = float(input('Digite o peso do lutador: '))

if peso < 65:
    categoria = 'Pena'
elif peso < 72:
    categoria = 'Leve'
elif peso < 79:
    categoria = 'Ligeiro'
elif peso < 86:
    categoria = 'Meio médio'
elif peso < 93:
    categoria = 'Médio'
elif peso < 100:
    categoria = 'Meio pesado'
else:
    categoria = 'Pesado'

answer = 'O lutador {} pesa {:.1f} kg e se enquadra na categoria {}'
print(answer.format(nome, peso, categoria))

print('Fim do programa')