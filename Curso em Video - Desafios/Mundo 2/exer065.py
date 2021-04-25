# crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
# a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve 
# perguntar ao usuário se ele quer ou não continuar a digitar valores

sumNumbers = qtdNumbers = 0
moreNumbers = 'S'
while moreNumbers in 'Ss':
    number = int(input('digite um número inteiro: '))

    sumNumbers += number
    qtdNumbers += 1
    
    if qtdNumbers == 1:
        bigger = smaller = number
    elif number > bigger:
        bigger = number
    elif number < smaller:
        smaller = number

    moreNumbers = input('digitar mais um número inteiro (S/N): ').strip().upper()

average = sumNumbers / qtdNumbers

print('Quantidade de valores digitados: {}'.format(qtdNumbers))
print('Soma dos valores: {}'.format(sumNumbers))
print('Média: {}'.format(average))
print('Maior valor: {}'.format(bigger))
print('Menor valor: {}'.format(smaller))
