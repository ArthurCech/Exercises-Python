# faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

number = int(input('digite um número inteiro: '))

predecessor = number - 1
successor = number + 1

print('\033[1;33mAntecessor: \033[1;31m{}\033[m'.format(predecessor))
print('\033[1;33mSucessor: \033[1;31m{}\033[m'.format(successor))
