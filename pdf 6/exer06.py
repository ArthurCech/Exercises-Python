# Leia dois números inteiros LMin e LMax. Em seguida leia 10 valores inteiros e inserindo-os em uma lista A somente se o valor fornecido estiver no intervalo [LMin, LMax]. Valores fora deste intervalo devem ser ignorados. Ao final, apresentar a lista A e seu tamanho efetivo. Observe que para este programa funcionar apropriadamente é necessário que LMin seja menor que LMax. Caso o usuário digite LMax menor que LMin, o programa deve inverter os valores.

LMin = int(input('digite o valor mínimo: '))

LMax = LMin
while LMax == LMin:
    LMax = int(input('digite o valor máximo: '))

if LMax < LMin:
    LMin, LMax = LMax, LMin

listNumbers = []
for i in range(10):
    number = int(input('digite um número inteiro: '))
    if LMin <= number <= LMax:
        listNumbers.append(number)

print('Quantidade de elementos da lista: {}'.format(len(listNumbers)))
print(listNumbers)
