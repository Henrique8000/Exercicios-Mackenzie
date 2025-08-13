"""
4. Faça um programa que peça as quatro notas (entre 0 e 10) de 10 alunos. Calcule e armazene
numa lista a média de cada aluno. Mostre esta lista e imprima o número de alunos com média
maior ou igual a 7.0. Para esta questão você deverá implementar 2 SOLUÇÕES - uma sem utilizar funções e a outra
solução utilizando funções.
"""


#Com Função

def main():
    medias = []
    qtd_medias = entra_nota(medias)
    media_maior_igual_7(qtd_medias)


def entra_nota(lm):
    notas = []
    n_aluno = 1

    for i in range(3):
        print(f"<<<Notas do aluno{n_aluno}>>>")
        for a in range(4):
            print("\nInsira uma nota:")
            notas.append(float(input()))
        media = sum(notas) / len(notas)
        lm.append(media)
        n_aluno += 1

    return lm


def media_maior_igual_7(m):
    qtd_alunos = 0

    for i in m:
        if i >= 7.0:
            qtd_alunos += 1

    print(f"A quantidade de alunos que tiraram 7.0 ou mais, foi: {qtd_alunos}")


main()
