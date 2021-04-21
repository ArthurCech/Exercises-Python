# Escreva um programa que leia uma lista com N números inteiros, onde N é um número inteiro previamente digitado pelo usuário. O programa não deve aceitar um número digitado que já esteja inserido na lista, sendo que quando esta situação ocorrer uma mensagem deve ser dada ao usuário. Por fim exibir na tela a lista resultante.

N = 0
while N <= 0:
    N = int(input('digite a quantidade de elementos: '))

listNumbers = []
i = 0
while i < N:
    number = int(input('digite um número inteiro: '))
    if number not in listNumbers:
        listNumbers.append(number)
        i += 1
    else:
        print('o número já está na lista')
    
print(listNumbers)
