print('\n1 - SACAR\n2 - DEPOSITAR\n3 - SAIR\n')
while True:
    op = int(input('\nDigite a opção desejada: '))

    match op:
        case 1:
            print('SAQUE REALIZADO')
        case 2:
            print('DEPÓSITO REALIZADO')
        case 3:
            print('SAÍDA COM SUCESSO')
            break
        case _:
            print('Inválido')

print('Programa Encerrado')
            
    