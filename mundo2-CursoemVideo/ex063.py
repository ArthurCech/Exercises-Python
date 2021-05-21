# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci

qtd_elements = int(input('digite a quantidade de elementos que deseja visualizar: '))

actual_element = 0
next_element = 1

for count in range(qtd_elements):
    print('{}  '.format(actual_element), end = '')
    last_element = actual_element
    actual_element = next_element
    next_element = last_element + actual_element
