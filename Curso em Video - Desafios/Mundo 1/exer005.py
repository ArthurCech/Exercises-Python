# faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

number = int(input('digite um número inteiro: '))

predecessor = number - 1
successor = number + 1

print('antecessor de {} = {}'.format(number, predecessor))
print('sucessor de {} = {}'.format(number, successor))

# economizar memória
print('antecessor de {} = {}'.format(number, number - 1))
print('sucessor de {} = {}'.format(number, number + 1))
