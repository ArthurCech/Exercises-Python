# sequência de fibonacci: 0, 1, 1, 2, 3, 5, 8, ...
# manipulação: o próximo é a soma dos dois anteriores

print('Exercício 09 do PDF Parte 4')

fileAnswer = open('exer09.txt', 'w')

qtd = 0
while qtd <= 0:
    qtd = int(input('Digite a quantidade de elementos que deseja visualizar: '))

i = 0
atual = 0
prox = 1
while i < qtd:
    print(atual, end=' ')
    print(atual, file=fileAnswer)
    ante = atual
    atual = prox
    prox = ante + atual
    i += 1

fileAnswer.close()

print('\nFim do programa')