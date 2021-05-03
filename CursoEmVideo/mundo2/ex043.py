# desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida

weight = float(input('digite o peso: '))
height = float(input('digite a altura: '))

imc = weight / (height ** 2)

if imc < 18.5:
    print('IMC: {:.2f} - Categoria: ABAIXO DO PESO'.format(imc))
elif imc < 25:
    print('IMC: {:.2f} - Categoria: PESO IDEAL'.format(imc))
elif imc < 30:
    print('IMC: {:.2f} - Categoria: SOBREPESO'.format(imc))
elif imc < 40:
    print('IMC: {:.2f} - Categoria: OBESIDADE'.format(imc))
else:
    print('IMC: {:.2f} - Categoria: OBESIDADE MÓRBIDA'.format(imc))
