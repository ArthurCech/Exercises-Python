# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci

qtdTerms = int(input('digite a quantidade de elementos que deseja visualizar: '))

i = 0
actualT = 0
nextT = 1
while i < qtdTerms:
    print('{}'.format(actualT), end=' ')
    lastT = actualT
    actualT = nextT
    nextT = lastT + actualT
    i += 1
