def main():
    nome = []
    curso = []
    nota = []

    entrada(nome, curso, nota)
    qtd_alunos_media(curso, nota)
    alunos_acima_media_curso(nome, curso, nota)


def entrada(a, b, c):
    menu = True
    while menu:
        a.append(input("Digite o nome do aluno: ").title())
        b.append(input("Digite o curso (CC, ADS ou SI): ").upper().strip())
        c.append(float(input("Digite a nota do aluno: ")))

        op = input("\nDeseja adicionar outro aluno s/n? ").lower()
        while op != 's' and op != 'n':
            print("\nInsira uma opção válida (s/n)\n")
            op = input("Deseja adicionar outro aluno s/n? ")

        if op == 'n':
            break


def qtd_alunos_media(c, n):
    indice = -1
    somacc = 0
    somasi = 0
    somaads = 0
    for i in c:
        indice += 1
        if i == 'CC':
            somacc += n[indice]

        elif i == 'SI':
            somasi += n[indice]

        elif i == 'ADS':
            somaads += n[indice]

    if c.count('CC') > 0:
        global mc
        mc = somacc / c.count('CC')
        print(f"\nQuantidade de alunos do curso de CC: {c.count('CC')}")
        print(f"Média dos alunos de CC: {mc:.2f}")
    else:
        print("\nNão foram cadastrados alunos em CC")

    if c.count('SI') > 0:
        global msi
        msi = somasi / c.count('SI')
        print(f"\nQuantidade de alunos do curso de SI: {c.count('SI')}")
        print(f"Média dos alunos de SI: {msi:.2f}")
    else:
        print("\nNão foram cadastrados alunos em SI")

    if c.count('ADS') > 0:
        global ma
        ma = somaads / c.count('ADS')
        print(f"\nQuantidade de alunos do curso de ADS: {c.count('ADS')}")
        print(f"{ma:.2f}")
    else:
        print("\nNão foram cadastrados alunos em ADS")


def alunos_acima_media_curso(nm, c, nt):
    indice = -1

    print("\nAlunos com nota acima da média do seu curso:")
    for i in nt:
        indice += 1
        if i > mc:
            print(f"Aluno: {nm[indice]} {c[indice]}")

        elif i > msi:
            print(f"Aluno: {nm[indice]} {c[indice]}")

        elif i > ma:
            print(f"Aluno: {nm[indice]} {c[indice]}")

        else:
            print()


main()