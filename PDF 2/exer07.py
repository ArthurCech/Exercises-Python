print('Exercício 07 do PDF Parte 2')

a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

if a != 0:
    delta = (b ** 2) - 4 * a * c
    
    if delta > 0:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print('Raíz X1 = {:.3f}'.format(x1))
        print('Raíz X2 = {:.3f}'.format(x2))
    elif delta == 0:
        x1 = -b / (2 * a)
        print('Raíz X = {:.3f}'.format(x1))
    else:
        print('Não existe raízes reais')
else:
    print('Não é uma equação de 2º grau!')

print('Fim do programa')