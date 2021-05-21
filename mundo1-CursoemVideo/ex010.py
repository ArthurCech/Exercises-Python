# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

reais = float(input('digite a quantia em reais: R$ '))

dolars = reais / 5.22

print('R$ {:.2f} = US$ {:.2f}'.format(reais, dolars))
