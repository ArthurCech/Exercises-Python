# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsidere o flag)

qtd_numbers = sum_numbers = 0

number = int(input('digite um número inteiro: '))

while number != 999:
    qtd_numbers += 1
    sum_numbers += number
    number = int(input('digite um número inteiro: '))

print('Quantidade de números digitados: {}'.format(qtd_numbers))
print('Soma dos números digitados: {}'.format(sum_numbers))
