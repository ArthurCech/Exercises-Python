# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

price = float(input('digite o preço do produto: R$ '))

final_price = price - (price * 0.05)

print('Preço com 5% de desconto: R$ {:.2f}'.format(final_price))
