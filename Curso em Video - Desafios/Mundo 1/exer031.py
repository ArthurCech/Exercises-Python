# desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da 
# passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens 
# mais longas

distance = float(input('digite a distância da viagem: '))

# forma simplificada
# priceTicket = distance * 0.50 if distance <= 200 else distance * 0.45

if distance <= 200:
    priceTicket = distance * 0.50
else:
    priceTicket = distance * 0.45

print('\033[1;32mValor da passagem: R$ {}\033[m'.format(priceTicket))
