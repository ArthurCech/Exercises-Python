# faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: A) quantidade de notas; B) a maior nota; C) a menor nota; D) a média da turma; E) a situação (opcional). Adicione também as docstrings da função

def notas(*grades, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param grades: notas dos alunos (aceita mais de uma nota)
    :param sit: (OPCIONAL) indica se deve aceitar a situação
    :return: dicionário com vários informações sobre a situação da turma
    """
    situation = dict()
    situation['total'] = len(grades)
    situation['maior'] = max(grades)
    situation['menor'] = min(grades)
    situation['media'] = sum(grades) / len(grades)

    if situation:
        if situation['media'] >= 7:
            situation['situacao'] = 'BOA'
        elif situation['media'] >= 5:
            situation['situacao'] = 'RAZOÁVEL'
        else:
            situation['situacao'] = 'RUIM'

    return situation


answer = notas(5.5, 2.5, 1.5, sit=True)
print(answer)
