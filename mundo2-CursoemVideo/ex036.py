# escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

house_price = float(input('digite o valor da casa: R$ '))
salary = float(input('digite o salário do comprador: R$ '))
years = int(input('digite a quantidade de anos da prestação: '))

monthly_value = house_price / (years * 12)
minimum_monthly_value = salary * 0.30

if monthly_value <= minimum_monthly_value:
    print('Empréstimo aprovado!')
    print('Prestação mensal: R$ {:.2f} em {} meses'.format(monthly_value, years * 12))
else:
    print('Empréstimo negado!')
