# escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado

quilometers = float(input('digite os quilometros percorridos: '))
days = int(input('digite a quantidade de dias: '))

final_price = days * 60 + quilometers * 0.15

print('Preço a pagar: R$ {:.2f}'.format(final_price))
