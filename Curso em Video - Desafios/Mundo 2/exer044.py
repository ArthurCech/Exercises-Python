# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# - a vista dinheiro/cheque: 10% de desconto
# - a vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

price = float(input('digite o valor total da compra: '))
print('''FORMAS DE PAGAMENTO:
( 1 ) à vista dinheiro/cheque   -   10% de desconto
( 2 ) à vista cartão            -   5% de desconto
( 3 ) 2x no cartão              -   preço normal
( 4 ) 3x ou mais no cartão      -   20% de juros''')
paymentMethod = int(input('digite a opção desejada: '))

if paymentMethod == 1:
    finalPrice = price - (price * 0.10)
elif paymentMethod == 2:
    finalPrice = price - (price * 0.05)
elif paymentMethod == 3:
    finalPrice = price
    paymentPerMonth = price / 2
    print('Compra parcelada em 2x de R$ {:.2f}'.format(paymentPerMonth))
elif paymentMethod == 4:
    finalPrice = price + (price * 0.20)
    months = int(input('digite a qtd. de parcelas: '))
    paymentPerMonth = finalPrice / months
    print('Compra parcelada em {}x de R$ {:.2f}'.format(months, paymentPerMonth))
else:
    print('Forma de pagamento inválida!')

print('Valor final: R$ {}'.format(finalPrice))
