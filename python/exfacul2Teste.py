def main():
    exibe_msg()
    opcao = opcao_F_ou_C()
    (inicial, final) = verifica_intervalo()

    if opcao == 'F':
        exibe_Fahrenheint(inicial, final)
    else:
        exibe_Celsius(inicial, final)


def exibe_msg():
    print('''
| Este programa tem como objetivo converter uma faixa de temperatura |
| de Fahrenheit para Celsius (para isso o usuário deve digitar F) e  |
| de Celsius para Fahrenheit (neste caso o usuário deve digitar C).  |
    ''')


def opcao_F_ou_C():
    op = input("Digite F, C ou 0 para sair: ").upper().strip()

    while op != 'F' and op != 'C':
        print("\nVocê precisa digitar corretamente ! (F ou C)\n")
        op = input("Digite F, C ou 0 para sair: ").upper().strip()


def verifica_intervalo():
    intervalo1 = int(input("Digite o início: "))
    intervalo2 = int(input("Digite o fim: "))

    while intervalo1 >= intervalo2:
        print("\nValores incorretos! O valor inicial deve ser menor que o valor final. Por favor, digite novamente.")
        intervalo1 = int(input("Digite o início: "))
        intervalo2 = int(input("Digite o fim: "))

    return intervalo1, intervalo2


def exibe_Fahrenheint(a, b):
    for i in range(a, b + 1, 1):
        c = (a - 32) / 1.8
        a += 1
        print(f'{c:.1f}')


def exibe_Celsius(x, y):
    for i in range(x, y + 1, 1):
        f = (x * 1.8) + 32
        x += 1
        print(f'{f:.1f}')


main()