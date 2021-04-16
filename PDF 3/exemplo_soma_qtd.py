print('Exemplo de quantidade de elementos')

soma = 0
qtde = 0
x = 1
while x != 0:
    x = int(input('Digite X:'))
    if x != 0:
        soma = soma + x
        qtde = qtde + 1

print('Total dos valores digitados = {}'.format(soma))
print('Quantidade de valores = {}'.format(qtde))

print('Fim do programa')