# crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
# valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1

money = int(input('digite o valor que deseja sacar: R$ '))
total = money
banknotes = 50
totbanknotes = 0
while True:
    if total >= banknotes:
        total -= banknotes
        totbanknotes += 1
    else:
        if totbanknotes > 0:
            print(f'Total de {totbanknotes} cédulas de R$ {banknotes}')
        if banknotes == 50:
            banknotes = 20
        elif banknotes == 20:
            banknotes = 10
        elif banknotes == 10:
            banknotes = 1

        totbanknotes = 0

        if total == 0:
            break
