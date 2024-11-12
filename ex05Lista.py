"""
5. Faça um programa em Python que leia duas listas – uma com peso e a outra com a altura de 5
pessoas. Construa uma lista de mesmo tamanho com o índice de massa corporal de cada pessoa
(IMC). IMC = peso/(altura)2
"""


def main():
    peso1 = float(input("Digite o peso da 1a pessoa: "))
    altura1 = float(input("Digite a altura da 1a pessoa: "))

    peso2 = float(input("\nDigite o peso da 2a pessoa: "))
    altura2 = float(input("Digite a altura da 2a pessoa: "))

    peso3 = float(input("\nDigite o peso da 3a pessoa: "))
    altura3 = float(input("Digite a altura da 3a pessoa: "))

    peso4 = float(input("\nDigite o peso da 4a pessoa: "))
    altura4 = float(input("Digite a altura da 4a pessoa: "))

    peso5 = float(input("\nDigite o peso da 5a pessoa: "))
    altura5 = float(input("Digite a altura da 5a pessoa: "))
    print()

    listaPeso = [peso1, peso2, peso3, peso4, peso5]
    listaAltura = [altura1, altura2, altura3, altura4, altura5]

    imc1 = 0.0
    imc2 = 0.0
    imc3 = 0.0
    imc4 = 0.0
    imc5 = 0.0

    liImc = calcula_imc(listaPeso, listaAltura)
    exibe_imc(liImc, listaPeso, listaAltura)


def calcula_imc(listaPeso, listaAltura):
    for indice in range(len(listaPeso)):

        if indice == 0:
            imc1 = listaPeso[indice] / (listaAltura[indice] ** 2)

        elif indice == 1:
            imc2 = listaPeso[indice] / (listaAltura[indice] ** 2)

        elif indice == 2:
            imc3 = listaPeso[indice] / (listaAltura[indice] ** 2)

        elif indice == 3:
            imc4 = listaPeso[indice] / (listaAltura[indice] ** 2)

        elif indice == 4:
            imc5 = listaPeso[indice] / (listaAltura[indice] ** 2)

    listaImc = [imc1, imc2, imc3, imc4, imc5]

    return listaImc


def exibe_imc(listaImc, listaPeso, listaAltura):
    for i in range(len(listaImc)):
        print(f"{i+1}a pessoa: peso = {listaPeso[i]:.1f}, altura = {listaAltura[i]:.2f} e imc = {listaImc[i]:.2f}")


main()
