num = int(input('Digite o numero: '))
a = 0
b = 1
print(b)
for i in range(1,num):
    a, b = b, b + a
    print(b)

#Outra maneira

'''a = 0
b = 1
aux = 1
print(aux)

for i in range(1, num):
    print(aux)
    a = b
    b = aux
    aux = a+b'''
