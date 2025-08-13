"""
3. Faça um programa que leia uma lista com 4 notas (entre 0 e 10), mostre as notas e a média na
tela. Para esta questão você deverá implementar 2 SOLUÇÕES - uma sem utilizar funções e a outra
solução utilizando funções.
"""

#Usando funções


def main():
    notas = []
    v_notas = ler_4_notas(notas)
    notas_e_media(v_notas)


def ler_4_notas(n):
    print("Insira 4 notas (0.0 - 10.0)")

    for i in range(4):
        n.append(float(input(">")))

    return n


def notas_e_media(x):
    print(f"As notas informadas são: {x}")
    media = (sum(x)) / len(x)

    if media >= 6.0:
        print("parabens!!! Você passou de ano!")
    else:
        print("Infelizmente você reprovou")

    print(f'A média final entre as quadro notas foi: {media:.2f}')


main()


#Sem funções
"""
def main():
    notas = []
    lista_notas = ler_4_entradas(notas)
    exibe_notas_media(lista_notas)


def ler_4_entradas(n):
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())

    n = [n1, n2, n3, n4]
    return n


def exibe_notas_media(n):
    soma = 0
    qtd_elementos = 0

    for i in n:
        soma += i
        qtd_elementos += 1

    media = soma / qtd_elementos

    print(f"As notas informadas são: {n}")
    print(f"A média final entre as quadro notas foi: {media:.2f}")


main()
"""