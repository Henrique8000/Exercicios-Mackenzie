carro = []
consumo = []


def main():
    entradaCarro()
    entradaConsumo()
    eco_carro = altoConsumo()
    print(eco_carro)


def entradaCarro():
    print("Insira 4 carros:")
    for i in range(4):
        carro.append(input())


def entradaConsumo():
    print("Insira o consumo dos 4 carros:")
    for i in range(4):
        consumo.append(int(input()))


def altoConsumo():
    print('\nO carro mais economico é:')
    indice = consumo.index(max(consumo))
    return carro[indice]


main()
