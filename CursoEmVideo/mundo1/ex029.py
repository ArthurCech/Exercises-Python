# escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite

velocity = float(input('digite a velocidade do carro: '))

if velocity > 80:
    trafficTicket = (velocity - 80) * 7
    print('\033[1;31mVocê foi multado em \033[1;32mR$ {:.2f}\033[m'.format(trafficTicket))
    
print('\033[1;33mDirija com cuidado!\033[m')
