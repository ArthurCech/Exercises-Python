# desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas

distance = float(input('digite a distância da viagem: '))

if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45

# if reduzido
price = distance * 0.50 if distance <= 200 else distance * 0.45

print('Preço da viagem: R$ {:.2f}'.format(price))
