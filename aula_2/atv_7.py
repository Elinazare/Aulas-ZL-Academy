num_lados= int(input('Digite a qtde de lados do polígono: '))
medida_lado = int(input('Digite a medida do lado: '))

if num_lados<3:
    print('não é um polígono')
elif num_lados==3:
    print('Triângulo. A área é: ', (medida_lado*medida_lado)/2)
elif num_lados==4:
    print('Quadrado. Área = ', medida_lado**2)
elif num_lados=='5': 
    print('Pentágono')
else: 
    print('polígono não identificado')