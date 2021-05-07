def show_list(list_numbers):
    '''Exibe na tela a lista de números primos'''
    for number in list_numbers:
        print(number)

def record_list(list_numbers, file_name):
    '''Grava o arquivo file_name com os elementos da lista de números primos, sendo um por linha'''
    file_primes = open(file_name, 'w')
    for number in list_numbers:
        file_primes.write('{}\n'.format(number))
    file_primes.close()
    
def is_prime(candidate):
    '''Verifica se o número candidato é primo (candidato deve ser um número inteiro)'''
    for count in range(2, candidate):
        if candidate % count == 0:
            return False
    return True

print('exercício 13')

quantity = int(input('digite a quantidade de números primos que deseja visualizar: '))

while quantity <= 0:
    quantity = int(input('[ERRO] digite a quantidade de números primos que deseja visualizar: '))

list_primes = []
candidate = 2
count = 0

while count < quantity:
    if is_prime(candidate):
        list_primes.append(candidate)
        count += 1
    candidate += 1

if quantity <= 20:
    print('Lista com os {} primeiros Primos'.format(quantity))
    show_list(list_primes)
else:
   print('Lista muito grande para exibição em tela.\nFoi gravado o arquivo primos.txt')
   record_list(list_primes, 'primos.txt')

print('fim do programa')
