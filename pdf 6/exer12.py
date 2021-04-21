# Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros digitados pelo usuário. Exiba na tela a lista preenchida. Em seguida, o programa deve procurar e eliminar os elementos que eventualmente estiverem repetidos deixando apenas a primeira ocorrência de cada valor. Apresentar a lista resultante na tela.

N = 0
while N <= 0:
    N = int(input('digite a quantidade de elementos: '))

listNumbers = []
for i in range(N):
    number = int(input('digite um número inteiro: '))
    listNumbers.append(number)

print(listNumbers)
print('tamanho original: {}'.format(len(listNumbers)))

i = 0
while i < len(listNumbers) - 1:
    j = i + 1
    while j < len(listNumbers):
        if listNumbers[i] == listNumbers[j]:
            del(listNumbers[j])
        else:
            j += 1
    i += 1

print(listNumbers)
print('tamanho após as remoções: {}'.format(len(listNumbers)))
