# Refaça o programa anterior, porém ao final exiba na tela cada elemento da lista em uma linha da tela (este programa deve exibir um elemento por vez dentro de um laço e usando um índice para acessar cada elemento individualmente).

listNumbers = []
number = 1
while number > 0:
    number = int(input('digite um número inteiro: '))
    if number > 0:
        listNumbers.append(number)

i = 0
while i < len(listNumbers):
    print(listNumbers[i])
    i += 1
