# Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida preencha uma lista com N elementos inteiros gerados aleatoriamente entre 0 e 1000 (usar a função randint)

from random import randint

qtd = 0
while qtd <= 0 or qtd > 50:
    qtd = int(input('digite a quantidade de valores: '))

listNumbers = []
for i in range(qtd):
    listNumbers.append(randint(0, 1000))

for number in listNumbers:
    print(number)
