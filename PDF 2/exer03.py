print('Exercício 03 do PDF Parte 2')

A = int(input('Digite um número inteiro: '))
B = int(input('Digite um número inteiro: '))

if A < B:
    print('O menor valor é A = {}'.format(A))
    print('O maior valor é B = {}'.format(B))
elif B < A:
    print('O menor valor é B = {}'.format(B))
    print('O maior valor é A = {}'.format(A))
else:
    print('Os valores A e B são iguais')

print('Fim do programa')