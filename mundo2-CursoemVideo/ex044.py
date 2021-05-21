# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

product_price = float(input('digite o preço do produto: R$ '))
print('''OPÇÕES DE PAGAMENTO:
(1) - à vista dinheiro/cheque: 10% de desconto
(2) - à vista no cartão: 5% de desconto
(3) - em até 2x no cartão: preço normal
(4) - 3x ou mais no cartão: 20% de juros''')
option = int(input('digite a opção desejada: '))

if option == 1:
    final_price = product_price - (product_price * 0.10)
    print('Opção de pagamento: à vista dinheiro/cheque (10% de desconto)')
    print('Preço final: R$ {:.2f}'.format(final_price))
elif option == 2:
    final_price = product_price - (product_price * 0.05)
    print('Opção de pagamento: à vista no cartão (5% de desconto)')
    print('Preço final: R$ {:.2f}'.format(final_price))
elif option == 3:
    monthly_value = product_price / 2
    print('Opção de pagamento: 2x no cartão (preço normal)')
    print('Valor da prestação: R$ {:.2f}'.format(monthly_value))
    print('Preço final: R$ {:.2f}'.format(product_price))
elif option == 4:
    qtd_months = int(input('digite a quantidade de meses: '))
    final_price = product_price * 1.20
    monthly_value = final_price / qtd_months
    print('{}x no cartão (20% de juros)'.format(qtd_months))
    print('Valor da prestação: R$ {:.2f}'.format(monthly_value))
    print('Preço final: R$ {:.2f}'.format(final_price))
else:
    print('Opção Inválida!')
