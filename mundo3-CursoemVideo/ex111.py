# crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos exercícios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from ex111_module.utilidadesCeV import moeda

price = float(input('digite o preço do item: R$ '))

moeda.resumo(price, 50, 25)
