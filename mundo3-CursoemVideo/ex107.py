# crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções

from ex107_module import moeda

price = float(input('digite o preço do item: R$ '))

print(f'Preço com aumento de 10%: R$ {moeda.aumentar(price, 10)}')
print(f'Preço com desconto de 15%: R$ {moeda.diminuir(price, 15)}')
print(f'Dobro do preço: R$ {moeda.dobro(price)}')
print(f'Metade do preço: R$ {moeda.metade(price)}')
