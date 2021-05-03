# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

price = float(input('digite o preço do produto: R$ '))
print('''DIGITE A OPÇÃO DE PAGAMENTO: 
( 1 ) - à vista dinheiro/cheque - 10% de desconto
( 2 ) - à vista no cartão - 5% de desconto
( 3 ) - em até 2x no cartão - preço normal
( 4 ) - 3x ou mais no cartão - 20% de juros''')
option = int(input('digite a opção do método de pagamento: '))

if option == 1:
    finalPrice = price - (price * 0.10)
    print('Opção de pagamento: à vista dinheiro/cheque')
    print('Desconto: 10%')
    print('Preço final: R$ {:.2f}'.format(finalPrice))
elif option == 2:
    finalPrice = price - (price * 0.05)
    print('Opção de pagamento: à vista no cartão')
    print('Desconto: 5%')
    print('Preço final: R$ {:.2f}'.format(finalPrice))
elif option == 3:
    finalPrice = price
    valueMonth = finalPrice / 2
    print('Opção de pagamento: 2x no cartão')
    print('Desconto: -')
    print('Prestação: R$ {:.2f}'.format(valueMonth))
    print('Preço final: R$ {:.2f}'.format(finalPrice))
elif option == 4:
    finalPrice = price * 1.20
    months = int(input('digite a quantidade de meses: '))
    valueMonth = finalPrice / months
    print('Opção de pagamento: {}x no cartão')
    print('Juros: 20%')
    print('Prestação: R$ {:.2f}'.format(valueMonth))
    print('Preço final: R$ {:.2f}'.format(finalPrice))
else:
    print('Opção inválida!')
