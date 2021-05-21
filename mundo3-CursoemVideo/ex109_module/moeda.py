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
