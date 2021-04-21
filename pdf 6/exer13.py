# Escreva um programa que leia um número inteiro N. Em seguida calcule e armazene em uma lista os N primeiros números primos. Exibir a lista no final.

def ExibirLista(listPrimes):
    '''Exibe na tela a lista de primos'''
    for a in listPrimes:
        print(a)

def GravarArquivo(listPrimes, fileName):
    '''Grava a lista de primos em um arquivo'''
    arq = open(fileName, 'w')
    for p in listPrimes:
        arq.write('{}\n'.format(p))
    arq.close()

def isPrime(candidate):
    '''Verifica se o num. candidato é primo. Candidato deve ser num. inteiro'''
    for i in range(2, candidate):
        if candidate % i == 0:
            return False
    return True

N = 0
while N <= 0:
    N = int(input('digite a quantidade de elementos: '))

listPrimes = []
candidate = 2
i = 0
while i < N:
    if isPrime(candidate):
        listPrimes.append(candidate)
        i += 1
    candidate += 1

if N <= 20:
    print('Lista com os {} Primos'.format(N))
    ExibirLista(listPrimes)
else:
   print('Arquivo gravado com sucesso!')
   GravarArquivo(listPrimes, 'primos.txt')
