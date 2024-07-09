'''Desenvolver um algoritmo que leia um número não determinado de valores e
calcule e escreva a média aritmética dos valores lidos, a quantidade de valores
positivos, a quantidade de valores negativos e o percentual de valores
negativos e positivos.'''

qtde_positivos=0
qtde_negativos =0
soma = 0
i=0

print('0 - para sair')
while True:
    num = int(input('Número: '))
    
    if num==0:
        break
    
    if num>0:
        qtde_positivos +=1
    else:
        qtde_negativos +=1
        
    soma+=num
    i+=1

print(f'Qtde negativos: {qtde_negativos}')
print(f'Qtde positivos: {qtde_positivos}')
print(f'Percentual de positivos: {(qtde_positivos/i)*100:.0f} %')
print(f'Percentual de negativos: {(qtde_negativos/i)*100:.0f} %')
print(f'Media: {soma/i}')

    