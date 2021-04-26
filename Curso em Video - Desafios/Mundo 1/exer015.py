# escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o 
# carro custa R$ 60 por dia e R$ 0,15 por Km rodado.

kilometers = float(input('digite quantos quilometros foram percorridos: '))
days = int(input('digite a quantidade de dias que o carro foi alugado: '))

finalPrice = (days * 60) + (kilometers * 0.15)

print('\033[1;32mValor total a pagar: R$ {:.2f}\033[m'.format(finalPrice))
