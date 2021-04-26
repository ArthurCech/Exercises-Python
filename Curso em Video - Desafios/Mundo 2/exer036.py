# escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O 
# programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele 
# vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do 
# salário ou então o empréstimo será negado

priceHouse = float(input('digite o preço da casa: R$ '))
salary = float(input('digite o salário: R$ '))
years = int(input('digite a quantidade de anos que pretende pagar: '))

installment = priceHouse / (years * 12)
thirtyPercentSalary = salary * 0.30

print('Valor da prestação: R$ {:.2f}'.format(installment))
print('Meses a pagar: {}'.format(years * 12))

if installment <= thirtyPercentSalary :
    print('Situação do empréstimo: APROVADO')    
else:
    print('Situação do empréstimo: NEGADO')
