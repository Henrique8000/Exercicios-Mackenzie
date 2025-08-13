"""
Implemente um programa que permita ao usuário cadastrar uma lista de alunos, sendo que:
    – O programa deve solicitar o nome do aluno, a nota que ele tirou na P1 e na P2.
    Deverá ser calculada a média de cada aluno e, também, qual o resultado (aprovado, se a média for maior
    ou igual a 6 ou reprovado, caso contrário)
    – As informações de cada aluno devem ser armazenadas em um dicionário
    – Os dados de todos os alunos devem ser armazenados em uma lista de dicionários.
"""


def main():
    lista_alunos = []
    menu = True
    l_aluno = entrada(lista_alunos)

    while menu:
        op = input("\nDeseja adicionar outro aluno? ")
        if op == 's':
            l_aluno = entrada(lista_alunos)

        elif op == 'n':
            print()
            exibe_resultado(l_aluno)
            break

        else:
            print('Digite uma opção válida!!!(s - n)\n')


def entrada(l_alunos):
    aluno = {}
    aluno["nome"] = input("Digite seu nome: ")
    aluno["p1"] = float(input("Digite a nota da P1: "))
    aluno["p2"] = float(input("Digite a nota P2: "))
    aluno["media"] = (aluno["p1"] + aluno["p2"]) / 2
    aluno["resultado"] = "peso"

    if aluno["media"] >= 6:
        aluno["resultado"] = "Aprovado"

    else:
        aluno["resultado"] = "Reprovado"

    l_alunos.append(aluno)

    return l_alunos


def exibe_resultado(l_alunos):
    print(f"Dados dos alunos: {l_alunos}\n")

    for i in l_alunos:
        print(f"Nome: {i["nome"]}\nPeso: {i["resultado"]}\n")


main()
