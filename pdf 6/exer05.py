# Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50 – o programa deve garantir isso em um laço) e em seguida leia N números reais em uma lista A. O programa deve separar os valores lidos em A em outras duas listas NEG e POS, a primeira contendo somente os valores negativos e a segunda contendo os valores positivos e zero. Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma.

qtd = 0
while qtd <= 0 or qtd > 50:
    qtd = int(input('digite a quantidade de valores: '))

listNumbersA = []
listNeg = []
listPos = []
for i in range(qtd):
    number = int(input('digite um número inteiro: '))
    listNumbersA.append(number)

    if number >= 0:
        listPos.append(number)
    else:
        listNeg.append(number)

print('Quantidade de elementos positivos: {}'.format(len(listPos)))
print(listPos)
print('Quantidade de elementos negativos: {}'.format(len(listNeg)))
print(listNeg)
