print('exercício 8')

side_a = float(input('digite o valor do lado A: '))
while side_a <= 0:
    side_a = float(input('digite o valor do lado A: '))

side_b = float(input('digite o valor do lado B: '))
while side_b <= 0:
    side_b = float(input('digite o valor do lado B: '))

side_c = float(input('digite o valor do lado C: '))
while side_c <= 0:
    side_c = float(input('digite o valor do lado C: '))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print('Os valores (A = {:.2f} e B = {:.2f} e C = {:.2f}) formam um triângulo'.format(side_a, side_b, side_c), end = ' ')

    if side_a == side_b == side_c:
        print('\033[1;33mequilátero\033[m')
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print('\033[1;33misósceles\033[m')
    else:
        print('\033[1;33mescaleno\033[m')
else:
    print('Os valores (A = {:.2f} e B = {:.2f} e C = {:.2f}) não formam um triângulo'.format(side_a, side_b, side_c))

print('fim do programa')
