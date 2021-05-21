# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salary = float(input('digite o salário do funcionário: R$ '))

final_salary = salary * 1.15

print('Salário com 15% de aumento: R$ {:.2f}'.format(final_salary))
