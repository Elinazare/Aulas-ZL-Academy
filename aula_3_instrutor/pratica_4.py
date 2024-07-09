votoBN =0
votoA=0
votoB=0

while True:
    print('0 - Bracos e nulos\n1 - Aldemir\n2- Bruna\n')
    op = int(input('Digite o candidato escolhido: '))

    match op:
        case 0:
            votoBN +=1
        case 1:
            votoA +=1
        case 2:
            votoB +=1
        case _:
            break
        
print(f'Qtde de votos - Ademir: {votoA}')
print(f'Qtde de votos - Bruna: {votoB}')
print(f'Qtde de votos - brancos e nulos: {votoBN}')