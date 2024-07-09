A = int(input())
B = int(input())

print('\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n')
op = int(input('Escolha a opção: '))

match op:
    case 1:
        print('Soma = ', A+B)
    case 2:
        print('Subtração = ', A-B)
    case 3: 
        print('Multiplicação = ', A*B)
    case 4: 
        print('Divisão = ', A/B)
    case _:
        print('Operação não encontrada')

        