#Exemplos durante a aula

#print('Maria')
'''var = input() 
print(var)'''



'''var = 5
var +=6
print(var)'''

'''var =5
var -=6
print(var)'''


#imprimir tipo da variavel
'''var =5
print(type(var))

nome="Eli"
print(type(nome))'''

#operações aritiméticas - sub
'''A = int(input())
B= int(input())
sub = A-B
print(sub)

#operações aritiméticas - mult
A = int(input())
B= int(input())
mult = A*B
print(mult)

#operações aritiméticas - divisao
A = int(input())
B= int(input())
divisao = A/B
print(divisao)'''

#"A soma de" + str(A) + "+" + str(B)


'''#operações aritiméticas - soma
A = int(input())
B= int(input())
soma = A+B
#print("A soma é igual a: %i" %soma)
#print(f'A soma é igual a: {soma}')
print('A soma é {:d}'.format(soma))
print(' A soma é:'+ str(soma))'''

nome = input('nome: ')
altura = float(input('altura: '))
#print(f'A altura de {nome} é {altura}')
#print('A %s tem  %.2f de altura' %(nome, altura) )
#print('A altura de ' + nome + " é "  + str(altura))
print('A altura de {:s} é igual a {:.2f}'.format(nome,altura))

