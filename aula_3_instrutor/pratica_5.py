soma_notas = 0
cont=0

while True:

    N = int(input('Digite a nota: '))

    if N < 0:
        break
    elif N > 10:
        print('Nota Inválida')
    else:
        soma_notas += N
        cont += 1

print(f'Média: {soma_notas/cont:.1f}')
        
