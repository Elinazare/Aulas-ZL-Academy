print('1 - SACAR\n2 - DEPOSITAR\n3 - CANCELAR\n')

op = int(input('Escolha a opção: '))

match op:
    case 1:
        print('SAQUE REALIZADO')
    case 2:
        print('DEPÓSITO REALIZADO')
    case 3:
        print('OPERAÇÃO CANCELADA')
    case _:
        print('OPÇÃO INVÁLIDA')
