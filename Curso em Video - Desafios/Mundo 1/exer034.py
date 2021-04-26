# escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu 
# aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para 
# inferiores ou iguais, aumento de 15%

salary = float(input('digite o salário do funcionário: '))

# forma simplificada
# newSalary = salary * 1.10 if salary > 1250 else salary * 1.15

if salary > 1250:
    newSalary = salary * 1.10
else:
    newSalary = salary * 1.15

print('\033[1;32mSalário reajustado: R$ {:.2f}\033[m'.format(newSalary))
