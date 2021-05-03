# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salary = float(input('digite o salário do funcionário: R$ '))

salaryIncrease = salary * 1.15

print('\033[1;33mSalário com 15% de aumento: \033[1;31mR$ {:.2f}\033[m'.format(salaryIncrease))
