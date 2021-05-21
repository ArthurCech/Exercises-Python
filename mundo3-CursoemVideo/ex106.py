# faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palara 'FIM', o programa se encerrará

c = ('\033[m',          # 0 - sem cor
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
    );   


def ajuda(command):
    titulo(f'Manual do comando \'{command}\'', 4)
    print(c[6], end='')
    help(command)
    print(c[0], end='')


def titulo(message, color=0):
    length = len(message) + 4
    print(c[color], end='')
    print('~' * length)
    print(f'  {message}')
    print('~' * length)
    print(c[0], end='')


command = ''

while True:
    titulo('SISTEMA DE AJUDA', 2)
    command = input('Função ou biblioteca > ')
    
    if command.upper() == 'FIM':
        break
    else:
        ajuda(command)
