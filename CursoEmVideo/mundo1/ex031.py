# desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas

distance = float(input('digite a distância da viagem: '))

if distance <= 200:
    ticketPrice = distance * 0.50
else:
    ticketPrice = distance * 0.45

# if reduzido
# ticketPrice = distance * 0.50 if distance <= 200 else distance * 0.45

print('\033[1;33mValor da passagem: \033[1;31mR$ {:.2f}\033[m'.format(ticketPrice))
