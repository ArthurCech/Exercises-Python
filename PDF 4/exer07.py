print('Exercício 07 do PDF Parte 4')

fileAnswer = open('exer07.txt', 'w')

qtd = 0
soma = 0
num = 1
while num > 0:
    num = int(input('Digite um número inteiro: '))
    if num > 0:
        if qtd == 0:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        qtd += 1
        soma += num

media = soma / qtd

print('Maior valor = {}'.format(maior))
print('Menor valor = {}'.format(menor))
print('Quantidade de valores = {}'.format(qtd))
print('Soma dos valores = {}'.format(soma))
print('Media dos valores = {}'.format(media))

print('Maior valor = {}'.format(maior), file=fileAnswer)
print('Menor valor = {}'.format(menor), file=fileAnswer)
print('Quantidade de valores = {}'.format(qtd), file=fileAnswer)
print('Soma dos valores = {}'.format(soma), file=fileAnswer)
print('Media dos valores = {}'.format(media), file=fileAnswer)

fileAnswer.close()

print('Fim do programa')