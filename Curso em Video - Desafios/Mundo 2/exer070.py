# crie um programa que leia o nome e o preço de vários produtos. O programa deverá 
# perguntar se o usuário vai continuar. No final, mostre:
# A) qual é o total gasto na compra
# B) quantos produtos custam mais de R$ 1000
# C) qual é o nome do produto mais barato

finalPrice = qtdProductsOver1000 = 0

moreProducts = 'S'
while moreProducts == 'S':
    nameProduct = input('digite o nome do produto: ').strip()
    priceProduct = float(input('digite o preço do produto: '))

    if finalPrice == 0:
        priceCheapestProduct = priceProduct
        nameCheapestProduct = nameProduct
    elif priceProduct < priceCheapestProduct:
        priceCheapestProduct = priceProduct
        nameCheapestProduct = nameProduct

    if priceProduct > 1000:
        qtdProductsOver1000 += 1

    finalPrice += priceProduct

    moreProducts = input('deseja inserir mais produtos (S/N): ').strip().upper()

print(f'Valor total da compra: R$ {finalPrice}')
print(f'Quantidade de produtos que custam mais de R$ 1000: {qtdProductsOver1000}')
print(f'Nome do produto mais barato: R$ {nameCheapestProduct}')
print(f'Preço do produto mais barato: R$ {priceCheapestProduct}')



# método guanabara
finalPrice = totOver1000 = priceCheapestProduct = count = 0
nameCheapestProduct = ''
while True:
    nameProduct = input('digite o nome do produto: ')
    priceProduct = float(input('digite o preço do produto: '))
    count += 1
    finalPrice += priceProduct

    if priceProduct > 1000:
        totOver1000 += 1

    if count == 1 or priceProduct < priceCheapestProduct:
        priceCheapestProduct = priceProduct
        nameCheapestProduct = nameProduct
    
    answer = ' '
    while answer not in 'SN':
        answer = input('deseja continuar (S/N): ').strip().upper()
    
    if answer == 'N':
        break

print(f'Valor total: R$ {finalPrice}')
print(f'Quantidade de produtos que custam mais de R$ 1000: {totOver1000}')
print(f'Nome do produto mais barato: {nameCheapestProduct}')
print(f'Preço do produto mais barato: {priceCheapestProduct}')
