# Refaça o exercício anterior generalizando-o para N valores inteiros digitados no teclado, onde N é um número fornecido pelo usuário. Esse N deve ser usado no programa ao invés do tamanho fixo de 10 sugerido no programa anterior.

LMin = int(input('digite o valor mínimo: '))

LMax = LMin
while LMax == LMin:
    LMax = int(input('digite o valor máximo: '))

if LMax < LMin:
    LMin, LMax = LMax, LMin

N = 0
while N <= 0:
    N = int(input('digite a quantidade de elementos: '))

listNumbers = []
for i in range(N):
    number = int(input('digite um número inteiro: '))
    if LMin <= number <= LMax:
        listNumbers.append(number)

print('Quantidade de elementos da lista: {}'.format(len(listNumbers)))
print(listNumbers)
