print('Exercício 08 do PDF Parte 2')

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

# a + b > c and a + c > b and b + c > a -> triângulo
if a > b + c or b > a + c or c > a + b:
    print('Não é um triângulo')
elif a == b and a == c:
    print('Triângulo equilátero ({}, {}, {})'.format(a, b, c))
elif a == b or a == c or b == c:
    print('Triângulo isósceles ({}, {}, {})'.format(a, b, c))
else:
    print('Triângulo escaleno ({}, {}, {})'.format(a, b, c))

print('Fim do programa')