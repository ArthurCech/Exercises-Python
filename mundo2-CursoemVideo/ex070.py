# crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) qual é o total gasto na compra; B) quantos produtos custam mais de R$ 1000; C) qual é o nome do produto mais barato

final_price = qtd_products_over1000 = count = price_smallest = 0

while True:
    product_name = input('digite o nome do produto: ')
    product_price = float(input('digite o preço do produto: '))

    count += 1
    final_price += product_price

    if count == 1 or product_price < price_smallest:
        name_smallest = product_name
        price_smallest = product_price

    if product_price > 1000:
        qtd_products_over1000 += 1

    add_products = input('deseja inserir mais produtos [S/N]: ').strip().upper()[0]
    while add_products not in 'SN':
        add_products = input('deseja inserir mais produtos [S/N]: ').strip().upper()[0]

    if add_products == 'N':
        break

print('Total gasto na compra: R$ {:.2f}'.format(final_price))
print('Qtd. de produtos que custam mais de R$ 1.000,00: {}'.format(qtd_products_over1000))
print('Nome do produto mais barato: {} - Preço: R$ {:.2f}'.format(name_smallest, price_smallest))
