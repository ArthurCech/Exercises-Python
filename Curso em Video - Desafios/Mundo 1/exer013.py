# faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário com 15% de aumento

salary = float(input('digite o salário do funcionário: '))

# newSalary = salary + (salary * 15 / 100)
newSalary = salary * 1.15

print('\033[1;32mSalário com aumento de 15%: R$ {:.2f}\033[m'.format(newSalary))
