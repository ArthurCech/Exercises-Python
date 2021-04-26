# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar 
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre 
# quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

countNumbers = sumNumbers = number = 0
number = int(input('digite um número inteiro: '))
while number != 999:
    countNumbers += 1
    sumNumbers += number
    number = int(input('digite um número inteiro: '))

print('Soma dos números: {}'.format(sumNumbers))
print('Quantidade de números digitados: {}'.format(countNumbers))
