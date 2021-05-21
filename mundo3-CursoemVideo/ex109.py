# modifique as funções que foram criadas no exercício 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no exercício 108

from ex109_module import moeda

price = float(input('digite o preço do item: R$ '))

print(f'Preço com aumento de 10%: {moeda.aumentar(price, 10, True)}')
print(f'Preço com desconto de 15%: {moeda.diminuir(price, 15, True)}')
print(f'Dobro do preço: R$ {moeda.dobro(price, True)}')
print(f'Metade do preço: R$ {moeda.metade(price, True)}')
