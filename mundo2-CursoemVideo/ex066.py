# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsidere o flag)

sum_numbers = qtd_numbers = 0
while True:
    number = int(input(f'digite o {qtd_numbers + 1}º número (999 para sair): '))

    if number == 999:
        break

    sum_numbers += number
    qtd_numbers += 1

print('Quantidade de números digitados: {}'.format(qtd_numbers))
print('Soma dos números digitados: {}'.format(sum_numbers))
