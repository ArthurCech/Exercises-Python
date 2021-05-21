# crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

add_number = 'S'
qtd_numbers = sum_numbers = 0

while add_number == 'S':
    number = int(input('digite um número inteiro: '))

    qtd_numbers += 1
    sum_numbers += number

    if qtd_numbers == 1:
        biggest_number = smallest_number = number
    elif number > biggest_number:
        biggest_number = number
    elif number < smallest_number:
        smallest_number = number

    add_number = input('digitar mais um número [S/N]? ').strip().upper()[0]

average = sum_numbers / qtd_numbers

print('Média dos valores digitados: {:.2f}'.format(average))
print('Maior valor digitado: {}'.format(biggest_number))
print('Menor valor digitado: {}'.format(smallest_number))
