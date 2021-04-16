print('Exercício 10 do PDF Parte 4')

fileAnswer = open('exer10.txt', 'w')



qtd = 0
while qtd <= 0:
    qtd = int(input('Digite a quantidade de elementos que deseja visualizar: '))

prim = int(input('Digite o valor inicial mínimo: '))

i = 0
atual = 0
prox = 1
ante = 0
while i < qtd:
    if atual >= prim:
        print(atual, end=' ')
        print(atual, file=fileAnswer)
        i += 1
    ante = atual
    atual = prox
    prox = ante + atual

fileAnswer.close()

print('Fim do programa')