"""
5. Faça um programa em Python que leia duas listas – uma com peso e a outra com a altura de 5
pessoas. Construa uma lista de mesmo tamanho com o índice de massa corporal de cada pessoa
(IMC). IMC = peso/(altura)2
"""

listaPeso = []
listaAltura = []
lista_imc = []
n_pessoa = 1


for i in range(5):
    listaPeso.append(float(input(f"Digite o peso da {n_pessoa}a pessoa: ")))
    listaAltura.append(float(input(f"Digite a altura da {n_pessoa}a pessoa: ")))
    print()
    n_pessoa += 1

for indice in range(len(listaPeso)):

    if indice == 0:
        lista_imc.append(listaPeso[indice] / (listaAltura[indice] ** 2))

    elif indice == 1:
        lista_imc.append(listaPeso[indice] / (listaAltura[indice] ** 2))

    elif indice == 2:
        lista_imc.append(listaPeso[indice] / (listaAltura[indice] ** 2))

    elif indice == 3:
        lista_imc.append(listaPeso[indice] / (listaAltura[indice] ** 2))

    elif indice == 4:
        lista_imc.append(listaPeso[indice] / (listaAltura[indice] ** 2))


for i in range(len(lista_imc)):
    print(f"{i+1}a pessoa: peso = {listaPeso[i]:.1f}, altura = {listaAltura[i]:.2f} e imc = {lista_imc[i]:.2f}")
