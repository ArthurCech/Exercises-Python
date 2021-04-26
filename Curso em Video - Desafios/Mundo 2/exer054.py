# crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas 
# pessoas ainda não atingiram a maioridade e quantas já são maiores

sumAdultHood = 0
for i in range(7):
    year = int(input('digite o ano de nascimento da pessoa {}: '.format(i + 1)))
    
    if year >= 21:
        sumAdultHood += 1

print('Quantidade de pessoas que atingiram a maioridade: {}'.format(sumAdultHood))
