soma = 0
qtde = 0
X = 1
while X != 0:
    X = int(input('digite X: '))
    if X != 0:
        soma = soma + X
        qtde = qtde + 1

print('Total de valores digitados = {}'.format(soma))
print('Quantidade de valores = {}'.format(qtde))
