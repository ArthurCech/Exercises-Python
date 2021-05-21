# faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

number = int(input('digite o número: '))

predecessor = number - 1
successor = number + 1

print('Antecessor: {}'.format(predecessor))
print('Sucessor: {}'.format(successor))
