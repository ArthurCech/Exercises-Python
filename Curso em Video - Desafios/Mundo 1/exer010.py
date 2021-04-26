# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos 
# dólares ela pode comprar. Considere US$ 1,00 = R$ 5,49

quantityReais = float(input('digite a quantidade de reais que possui: '))

quantityDolars = quantityReais / 5.49
quantityLibras = quantityReais / 7.60

print('Com R$ {:.2f} você compra US$ {:.2f}'.format(quantityReais, quantityDolars))
print('Com R$ {:.2f} você compra £ {:.2f}'.format(quantityReais, quantityLibras))
