def aumentar(price=0, percent=0, formating=False):
    res = price + (price * percent / 100)
    return res if formating is False else moeda(res)


def diminuir(price=0, percent=0, formating=False):
    res = price - (price * percent / 100)
    return res if formating is False else moeda(res)


def dobro(price=0, formating=False):
    res = price * 2
    return res if formating is False else moeda(res)


def metade(price=0, formating=False):
    res = price / 2
    return res if formating is False else moeda(res)


def moeda(price=0, money='R$'):
    return f'{money} {price:>.2f}'.replace('.', ',')


def resumo(price=0, percent_increase = 10, percent_reduction=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço: \t{moeda(price)}')
    print(f'Preço com aumento de {percent_increase}%: \t{aumentar(price, percent_increase, True)}')
    print(f'Preço com redução de {percent_reduction}%: \t{diminuir(price, percent_reduction, True)}')
    print(f'Dobro do preço: \t\t{dobro(price, True)}')
    print(f'Metade do preço: \t\t{metade(price, True)}')
    print('-' * 30)
