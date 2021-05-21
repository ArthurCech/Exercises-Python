# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados de forma tabular

products = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)

for count in range(len(products)):
    if count % 2 == 0:
        print('{:.<30}'.format(products[count]), end = '')
    else:
        print('R$ {:>7.2f}'.format(products[count]))

print('-' * 40)
