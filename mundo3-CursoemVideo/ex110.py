# adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui

from ex110_module import moeda

price = float(input('digite o preço do item: R$ '))

moeda.resumo(price, 20, 10)
