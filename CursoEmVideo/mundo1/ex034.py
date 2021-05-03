# escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salary = float(input('digite o salário do funcionário: R$ '))

if salary > 1250:
    salaryWithIncrease = salary * 1.10
else:
    salaryWithIncrease = salary * 1.15
    
print('\033[1;33mSalário com aumento: \033[1;31mR$ {:.2f}\033[m'.format(salaryWithIncrease))
