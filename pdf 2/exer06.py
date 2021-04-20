# Escreva um programa que leia o nome de um lutador e seu peso. Em seguida informe a 
# categoria a que pertence o lutador, conforme a tabela abaixo. A saída do programa deve 
# exibir na tela um texto no seguinte padrão: Nome fornecido: Pepe Jordão - Peso fornecido: 73.4
# Saída exibida na tela: O lutador Pepe Jordão pesa 73.4 kg e se enquadra na categoria Ligeiro

# Peso                                          Categoria
# Menor que 65 kg                               Pena
# Maior ou igual a 65 kg e menor que 72 kg      Leve
# Maior ou igual a 72 kg e menor que 79 kg      Ligeiro
# Maior ou igual a 79 kg e menor que 86 kg      Meio médio
# Maior ou igual a 86 kg e menor que 93 kg      Médio
# Maior ou igual a 93 kg e menor que 100 kg     Meio pesado
# Maior ou igual a 100 kg                       Pesado

name = input('digite o nome do lutador: ')
weight = float(input('digite o peso do lutador: '))

if weight < 65:
    category = 'Pena'
elif weight < 72:
    category = 'Leve'
elif weight < 79:
    category = 'Ligeiro'
elif weight < 86:
    category = 'Meio médio'
elif weight < 93:
    category = 'Médio'
elif weight < 100:
    category = 'Meio pesado'
else:
    category = 'Pesado'

msg = 'O lutador {} pesa {:.1f} kg e se enquadra na categoria {}'
print(msg.format(name, weight,  category))
