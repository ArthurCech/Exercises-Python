# escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

priceHouse = float(input('digite o preço da casa: R$ '))
salary = float(input('digite o salário do comprador: R$ '))
years = int(input('digite a quantidade de anos para quitar o pagamento: '))

monthlyValue = priceHouse / (years * 12)
minMonthlyValue = salary * 0.30

print('Valor da prestação: {:.2f}'.format(monthlyValue))

if monthlyValue <= minMonthlyValue:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
