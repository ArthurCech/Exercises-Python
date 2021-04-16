print('Exercício 02 do PDF Parte 2')

A = int(input('Digite um número inteiro: '))
B = int(input('Digite um número inteiro: '))

if A < B:
    print('O menor valor é o A = {}'.format(A))
elif B < A:
    print('O menor valor é o B = {}'.format(B))
else:
    print('Os números são iguais')

print('Fim do programa')