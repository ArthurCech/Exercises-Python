# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

price = float(input('digite o preço do item: '))

# newPrice = price - (price * 5 / 100)
newPrice = price - (price * 0.05)

print('\033[1;32mPreço do produto com 5% de desconto: R$ {:.2f}\033[m'.format(newPrice))
