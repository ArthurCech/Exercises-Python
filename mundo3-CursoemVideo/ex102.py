# crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(number, show=False):
    """
    -> Calcula o fatorial do número passado como parâmetro
    :param number: fatorial a ser calculado
    :param show: (OPCIONAL) mostrar o resultado
    :return: o valor do fatorial do número desejado
    """
    fact = 1

    for count in range(number, 0, -1):
        if show:
            print(count, end='')
            if count > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fact *= count

    return fact


number = int(input('digite o número que deseja calcular o fatorial: '))
show = bool(input('deseja mostrar na tela o resultado do fatorial [True/False]: '))
while show != True and show != False:
    show = bool(input('deseja mostrar na tela o resultado do fatorial [True/False]: '))

print(fatorial(number, show))
