lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if (lado1 + lado2 > lado3 and lado1 +lado3>lado2 and lado2+lado3>lado1):
    if(lado1==lado2==lado3):
        print('Equilátero')
    elif(lado1==lado2 or lado2==lado3 or lado1==lado3):
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Isso não é um triângulo')