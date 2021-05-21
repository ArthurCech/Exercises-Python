def aumentar(price, percent):
    res = price + (price * percent / 100)
    return res


def diminuir(price, percent):
    res = price - (price * percent / 100)
    return res


def dobro(price):
    res = price * 2
    return res


def metade(price):
    res = price / 2
    return res
