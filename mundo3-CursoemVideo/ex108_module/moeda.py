def aumentar(price=0, percent=0):
    res = price + (price * percent / 100)
    return res


def diminuir(price=0, percent=0):
    res = price - (price * percent / 100)
    return res


def dobro(price=0):
    res = price * 2
    return res


def metade(price=0):
    res = price / 2
    return res


def moeda(price=0, money='R$'):
    return f'{money} {price:>.2f}'.replace('.', ',')
