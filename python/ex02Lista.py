"""2. Faça um programa que leia uma lista de 10 números inteiros e mostre-os na ordem inversa da
digitação. Para esta questão você deverá implementar 2 SOLUÇÕES - uma sem utilizar funções e a outra
solução utilizando funções
"""

#Invertendo a lista utilizando funções
lista = []

for i in range(10):
    lista.append(int(input()))

lista.reverse()
print("\nImprimindo a lista 1")
print(lista)

#Invertendo a lista sem utilizar funções
lista2 = []

for k in range(10):
    lista2.append(int(input()))

print("\nImprimindo a lista 2")
print(lista2[::-1])
