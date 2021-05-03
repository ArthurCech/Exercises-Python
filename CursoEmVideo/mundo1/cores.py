print('\033[1;31;43mOlá, Mundo!\033[m')
print('{}Olá, Mundo!{}'.format('\033[1;36m', '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[7;30m'}
         
print('{}Olá, Mundo!{}'.format(cores['azul'], cores['limpa']))
