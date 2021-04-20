A = int(input('digite um valor para A: '))
B = int(input('digite um valor para B: '))
if B == 0:
    print('não é possível calcular a divisão')
else:
    R = A / B
    print('resultado: R = {:.1f}'.format(R))