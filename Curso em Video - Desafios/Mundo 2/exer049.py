# refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for

number = int(input('digite o número que deseja ver a tabuada: '))
print('-' * 11)
for i in range(1, 11):
    print('{} x {:2} = {}'.format(number, i, number * i))
print('-' * 11)
