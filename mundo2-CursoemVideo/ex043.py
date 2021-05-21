# desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: abaixo de 18.5 - abaixo do peso; entre 18.5 e 25 - peso ideal; 25 até 30 - sobrepeso; 30 até 40 - obesidade; acima de 40 - obesidade mórbida

height = float(input('digite a altura da pessoa: '))
weight = float(input('digite o peso da pessoa: '))

imc = weight / (height ** 2)

if imc < 18.5:
    category = 'abaixo do peso'
elif imc < 25:
    category = 'peso ideal'
elif imc < 30:
    category = 'sobrepeso'
elif imc < 40:
    category = 'obesidade'
else:
    category = 'obesidade mórbida'

print('IMC: {:.2f} - Categoria: {}'.format(imc, category))
