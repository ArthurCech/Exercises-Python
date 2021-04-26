# escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km 
# acima do limite.

velocity = float(input('digite a velocidade do carro: '))

if velocity > 80:
    print('\033[1;31mVocê foi multado!\033[m')
    priceTrafficTicket = 7 * (velocity - 80)
    print('\033[1;32mValor da multa: R$ {}\033[m'.format(priceTrafficTicket))
