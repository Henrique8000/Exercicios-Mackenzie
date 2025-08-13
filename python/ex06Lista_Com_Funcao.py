"""
Escreva um programa em Python que leia duas listas de 5 números inteiros cada e armazene em
uma lista de mesmo tamanho a soma de cada elemento das duas listas. Exibir as três listas.
Faça uma implementação sem funções e uma outra utilizando função. Na implementação com
funções NÃO UTILIZE variáveis GLOBAIS.
"""


def main():
    l1 = []
    l2 = []

    entrada_duas_listas(l1, l2)
    l_soma = soma(l1, l2)
    exibe_listas(l1, l2, l_soma)


def entrada_duas_listas(l1, l2):
    for k in range(1, 3, 1):
        print(f"Digite 5 números inteiros da lista{k}")

        if k == 1:
            for i in range(5):
                l1.append(int(input()))
        else:
            for n in range(5):
                l2.append(int(input()))


def soma(l1, l2):
    s_listas = []
    for indice in range(5):
        s_listas.append(l1[indice] + l2[indice])

    return s_listas


def exibe_listas(l1, l2, s):
    print(f"\nLista1: {l1}")
    print(f"Lista2: {l2}")
    print(f"Soma: {s}")


main()
