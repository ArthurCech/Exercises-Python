# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

sumNumbers = countNumbers = 0
while True:
    number = int(input('digite um número inteiro: '))
    if number == 999:
        break

    sumNumbers += number
    countNumbers += 1
    
print(f'Soma dos números: {sumNumbers}')
print(f'Quantidade de valores informados: {countNumbers}')
