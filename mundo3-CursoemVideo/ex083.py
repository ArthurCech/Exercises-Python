# crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expression = input('digite a expressão: ')

stack = list()

for character in expression:
    if character == '(':
        stack.append('(')
    elif character == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('A expressão está correta')
else:
    print('A expressão não está correta')
