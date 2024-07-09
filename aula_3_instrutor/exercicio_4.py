'''Faça um algoritmo estruturado que leia uma quantidade não determinada de
números positivos. Calcule a quantidade de números pares e ímpares, a média
de valores pares e a média geral dos números lidos. O número que encerrará a
leitura será zero.'''

num_par =0
num_impar=0
cont_par=0
cont_impar=0
i=0


while True:
    num = int(input('Número: '))
    
    match num:
        case 0:
            break
        case _:
            if num%2==0:
                num_par +=num
                cont_par +=1
            if num%2!=0:
                num_impar +=num
                cont_impar +=1
    i+=1
    
print(f'Qtde de numeros pares {cont_par}')
print(f'Qtde de numeros ímpares {cont_impar}')
print(f'Media dos numeros pares: {num_par/cont_par if cont_par!= 0 else 0}')
print(f'Média dos números lidos: {(num_impar + num_par)/i if i!=0 else 0}')

    

    