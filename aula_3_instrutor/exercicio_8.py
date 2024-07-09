'''Escreva um algoritmo que leia um valor A e imprima o resultado do cálculo
de A! (Fatorial.'''

A = int(input('Número : '))

fatorial = 1

for i in range(1, A+1):
    fatorial = fatorial*i
    
print(f'Fatorial de {A} é {fatorial}')
    