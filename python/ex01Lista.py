"""
1. Faça um programa que leia uma lista de 5 números inteiros e mostre-os.
Para esta questão você deverá implementar 2 SOLUÇÕES - uma sem utilizar funções e a outra
solução utilizando funções.
"""
lista = []
lista2 = []


#solução usando funções
def com_funcao(li):
    for i in range(5):
        num = li.append(int(input()))
    return li


#solução sem funções
def sem_funcao(li2):
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    li2 = [n1, n2, n3, n4, n5]

    return li2


chama1 = com_funcao(lista)
print(chama1)

chama2 = sem_funcao(lista2)
print(chama2)