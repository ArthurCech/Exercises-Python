print('Exercício 02 do PDF Parte 3')

n = 1
somaPositivo = 0
somaNegativo = 0
while n != 0:
    n = int(input('Digite um número inteiro: '))
    if n != 0:
        if n > 0:
            somaPositivo += n
        else:
            somaNegativo += n

print('Soma dos positivos = {}'.format(somaPositivo))
print('Soma dos negativos = {}'.format(somaNegativo))

print('Fim do programa')