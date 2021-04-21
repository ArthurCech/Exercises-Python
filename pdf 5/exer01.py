# Escreva um programa que permaneça em laço até que seja digitado o valor 
# zero ou negativo. Cada valor positivo lido deve ser inserido no final 
# de uma lista, usando o método append. Ao final exiba a lista completa na tela.

listNumbers = []
number = 1
while number > 0:
    number = int(input('digite um número inteiro: '))
    if number > 0:
        listNumbers.append(number)

print('*** LISTA ***')
print(listNumbers)
