# refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

number = int(input('digite um número inteiro: '))

for count in range(1, 11):
    print('{} x {:2} = {:2}'.format(number, count, number * count))
