# escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite

velocity = float(input('digite a velocidade do carro: '))

if velocity > 80:
    traffic_ticket = (velocity - 80) * 7
    print('Você ultrapassou o limite de 80 Km/h e foi multado em R$ {:.2f}'.format(traffic_ticket))

print('Dirija com atenção')
