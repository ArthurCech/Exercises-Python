# O programa deverá ler dois inteiros chamados Min e Max. Min pode ser qualquer valor e Max, obrigatoriamente, deve ser maior que Min. Em seguida preencher a lista com todos os valores situados entre Min e Max que sejam divisíveis por 7. Exibir a lista resultante na tela.

Min = int(input('digite o valor mínimo: '))

Max = Min
while Max <= Min:
    Max = int(input('digite o valor máximo: '))

listNumbers = []
for i in range(Min, Max + 1):
    if i % 7 == 0:
        listNumbers.append(i)

print(listNumbers)
