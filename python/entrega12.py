empresa = []
funcionario = []


def main():
    entradaEmpresa()
    entradaTotalFunc()
    emp_mais_func = maiorEmpresa()
    print(emp_mais_func)


def entradaEmpresa():
    for i in range(4):
        empresa.append(input())


def entradaTotalFunc():
    for i in range(4):
        funcionario.append(int(input()))


def maiorEmpresa():
    maior = 0
    indice = -1
    for k in funcionario:
        if k > maior:
            maior = k
            indice += 1
    return empresa[indice]


main()