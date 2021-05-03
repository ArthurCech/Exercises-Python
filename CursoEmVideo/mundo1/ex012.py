# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

price = float(input('digite o preço do produto: R$ '))

priceDiscount = price - (price * 0.05)

print('\033[1;33mPreço com 5% de desconto: \033[1;31mR$ {:.2f}\033[m'.format(priceDiscount))
