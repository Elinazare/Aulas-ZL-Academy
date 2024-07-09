#return true or false
'''num1 =5
num2=5
maior = num1>num2
#igual = num1==num2
print(maior)
#print(igual)'''

#verificar se A é maior que B
'''A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))

if A>B:
    print(f'Maior valor é {A}')
else:
    print(f'Maior valor é {B}')'''

#elif
'''A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))

if A>B:
    print(f'Maior valor é {A}')
elif(B>A):
    print(f'Maior valor é {B}') 
else:
    print(f'{A} é igual a {B}') '''

#Operadores lógicos(and, or e not)

#ex1  aprovado ou reprovado de acordo com a frequencia
'''nota = float(input('Nota: '))
frequencia = int(input('Frequência: '))

if (nota>=7.5 and frequencia>=75):
    print('Aprovado')
else:
    print('Reprovado')'''

#ex2 numero aceito se for impar ou negativo
'''num = int(input('Número: '))
if (num%2!=0 or num<0):
    print('Número aceito')
else:
    print('Número inválido')'''

#Ex sem operador lógico
idade = int(input('Digite a idade: '))

if idade<=13:
    print('Criança')
#elif 14<=idade<=59:
elif idade<=59:
    print('Jovem')
else:
    print('Idoso')

