# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 5,45

reais = float(input('digite a quantia em reais: R$ '))

dolares = reais / 5.45

print('\033[1;33mR$ {:.2f} = \033[1;31mUS$ {:.2f}\033[m'.format(reais, dolares))
