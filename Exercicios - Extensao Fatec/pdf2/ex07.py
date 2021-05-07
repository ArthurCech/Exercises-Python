print('exercício 7')

coefficient_a = float(input('digite o valor do coeficiente A: '))
coefficient_b = float(input('digite o valor do coeficiente B: '))
coefficient_c = float(input('digite o valor do coeficiente C: '))

if coefficient_a != 0:
    delta = pow(coefficient_b, 2) - 4 * coefficient_a * coefficient_c
    
    if delta > 0:
        x1 = (-coefficient_b + delta ** 0.5) / (2 * coefficient_a)
        x2 = (-coefficient_b - delta ** 0.5) / (2 * coefficient_a)
        print(' Raíz 1: {:.3f}'.format(x1))
        print(' Raíz 2: {:.3f}'.format(x2))
    elif delta == 0:
        x = -coefficient_b / (2 * coefficient_a)
        print(' Raíz: {:.3f}'.format(x))
    else:
        print(' Não existem raízes reais')
else:
    print('Não é uma equação de 2º grau completa')

print('fim do programa')
