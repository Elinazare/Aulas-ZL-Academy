'''Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa
deverá calcular e mostrar :
a. A menor altura do grupo;
b. A maior altura do grupo;'''

altura = float(input())

maior_altura=altura
menor_altura=altura

for i in range(0,14,1):
    altura = float(input())
    
    if altura>maior_altura:
        maior_altura =altura
    if altura < menor_altura:
        menor_altura =altura
print('Maior altura: ',maior_altura)
print('Menor altura: ',menor_altura)
    