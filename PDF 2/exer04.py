print('Exercício 04 do PDF Parte 2')

num = int(input('Digite um número inteiro: '))

if num == 0:
    print('O número informado {} é zero'.format(num))
elif num % 2 == 0:
    print('O número informado {} é um número par.'.format(num))
else:
    print('O número informado {} é um número ímpar'.format(num))

print('Fim do programa')