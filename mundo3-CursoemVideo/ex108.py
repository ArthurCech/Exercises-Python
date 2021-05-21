# adapte o código do exercício 107, criando uma função adicional chamado moeda() que consiga mostrar os valores como um valor monetário formatado

from ex108_module import moeda

price = float(input('digite o preço do item: R$ '))

print(f'Preço com aumento de 10%: {moeda.moeda(moeda.aumentar(price, 10))}')
print(f'Preço com desconto de 15%: {moeda.moeda(moeda.diminuir(price, 15))}')
print(f'Dobro do preço: R$ {moeda.moeda(moeda.dobro(price))}')
print(f'Metade do preço: R$ {moeda.moeda(moeda.metade(price))}')
