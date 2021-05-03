# escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado

quilometers = float(input('quantidade de quilometros percorridos pelo carro: '))
days = int(input('quantidade de dias que o carro foi alugado: '))

price = (days * 60) + (quilometers * 0.15)

print('\033[1;33mPreço a pagar: \033[1;31mR$ {:.2f}\033[m'.format(price))
