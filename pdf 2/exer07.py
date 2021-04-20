# Escreva um programa que leia três números reais A, B e C que são os coeficientes de 
# uma equação do 2º grau (A.x2 + B.x + C = 0). Calcule e apresente na tela as raízes 
# dessa equação, considerando os três casos possíveis: Delta maior que zero (duas 
# raízes reais), Delta igual a zero (uma raiz) e Delta menor que zero (não há raízes reais)

a = float(input('digite o coeficiente A: '))
b = float(input('digite o coeficiente B: '))
c = float(input('digite o coeficiente C: '))

if a == 0:
    print('não é uma equação de segundo grau completa!')
else:
    delta = (b ** 2) - 4 * a * c
    
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print('     x1 = {:.2f}'.format(x1))
        print('     x2 = {:.2f}'.format(x2))
    elif delta == 0:
        x = (-b) / (2 * a)
        print('     x = {:.2f}'.format(x))
    else:
        print('não existem raízes reais!')
