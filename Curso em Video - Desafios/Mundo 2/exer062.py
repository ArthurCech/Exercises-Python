# melhore o exer061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
# encerra quando ele disser que quer mostrar 0 termos.

firstTerm = int(input('digite o primeiro termo: '))
commonDifference  = int(input('digite a razão: '))

term = firstTerm
i = 0
tot = 0
moreTerms = 10

while moreTerms != 0:
    tot += moreTerms
    while i < tot:
        print('{}'.format(term), end=' ')
        term += commonDifference
        i += 1

    moreTerms = int(input('\ndeseja visualizar mais quantos termos: '))

print('Total de termos mostrados: {}'.format(tot))
