# crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues

amount = float(input('digite o valor a ser sacado: R$ '))

total_amount = amount
bank_note = 50
total_bank_note = 0

while True:
    if total_amount >= bank_note:
        total_amount -= bank_note
        total_bank_note += 1
    else:
        if total_bank_note > 0:
            print(f'Total de {total_bank_note} cédulas de R$ {bank_note}')
        if bank_note == 50:
            bank_note = 20
        elif bank_note == 20:
            bank_note = 10
        elif bank_note == 10:
            bank_note = 5
        elif bank_note == 5:
            bank_note = 2
        elif bank_note == 2:
            bank_note = 1

        total_bank_note = 0

        if total_amount == 0:
            break
