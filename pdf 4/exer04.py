# Reescreva um programa do exercício acima considerando exclusivamente os 
# números positivos fornecidos. Caso seja digitado zero ou um valor 
# negativo o programa deve exibir uma mensagem "número inválido" e o 
# valor deve ser ignorado.

answerFile = open('exer04.txt', 'w')

N = int(input('digite a quantidade de elementos: '))

i = 0
while i < N:
    valor = float(input('digite um número real: '))

    if valor <= 0:
        print('número inválido')
    else:
        if i == 0:
            maior = menor = valor
        elif valor >= maior:
            maior = valor
        elif valor <= menor:
            menor = valor

        i += 1

print('maior valor = {}'.format(maior))
print('menor valor = {}'.format(menor))

print('maior valor = {}'.format(maior), file=answerFile)
print('menor valor = {}'.format(menor), file=answerFile)

answerFile.close()
