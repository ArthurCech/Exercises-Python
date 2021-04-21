# Elaborar um programa que efetue a leitura de valores positivos inteiros até que zero ou um valor negativo seja informado. Ao final devem ser apresentados: o maior e menor valores informados pelo usuário, a quantidade de valores, a soma e a média de todos.

answerFile = open('exer07.txt', 'w')

qtd = 0
soma = 0
X = 1
while X > 0:
    X = int(input('digite um número inteiro: '))

    if X > 0:
        if qtd == 0:
            maior = menor = X
        elif X > maior:
            maior = X
        elif X < menor:
            menor = X
        
        qtd += 1
        soma += X

if qtd > 0:  
    media = soma / qtd
else:
    maior = menor = media = 0

print('Maior valor = {}'.format(maior))
print('Menor valor = {}'.format(menor))
print('Quantidade de valores = {}'.format(qtd))
print('Soma dos valores = {}'.format(soma))
print('Media = {}'.format(media))

# print('Maior valor = {}'.format(maior), file=answerFile)
# print('Menor valor = {}'.format(menor), file=answerFile)
# print('Quantidade de valores = {}'.format(qtd), file=answerFile)
# print('Soma dos valores = {}'.format(soma), file=answerFile)
# print('Media = {}'.format(media), file=answerFile)

answerFile.write('Maior valor = {}\n'.format(maior))
answerFile.write('Menor valor = {}\n'.format(menor))
answerFile.write('Quantidade de valores = {}\n'.format(qtd))
answerFile.write('Soma dos valores = {}\n'.format(soma))
answerFile.write('Media = {}\n'.format(media))

answerFile.close()
