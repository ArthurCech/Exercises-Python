# desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a tabela abaixo:
# menor que 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# entre 25 e 30: sobrepeso
# entre 30 e 40: obesidade
# acima de 40: obesidade mórbida

height = float(input('digite a altura da pessoa: '))
weight = float(input('digite o peso da pessoa: '))

# imc = peso / altura²
imc = weight / pow(height, 2.0)

if imc < 18.5:
    status = 'Abaixo do peso'
elif imc < 25:
    status = 'Peso ideal'
elif imc < 30:
    status = 'Sobrepeso'
elif imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade mórbida'

print('De acordo com o IMC: {:.2f}, você se enquadra no status: {}'.format(imc, status))
