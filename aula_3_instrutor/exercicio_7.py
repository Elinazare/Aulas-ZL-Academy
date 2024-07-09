'''Escreva um algoritmo que leia um valor inicial A e um valor final B e imprima
todos os números entre eles.'''

A = int(input('Valor inicial: '))
B = int(input('Valor final: '))

#usando for
'''for i in range(A+1,B,1):
    print(i)'''
 
#usando while
i = A+1
while i<B:
    print(i)
    i+=1