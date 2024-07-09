'''Desenvolver um algoritmo que efetue a soma de todos os números ímpares
que são múltiplos de três e que se encontram no conjunto dos números de 1
até 500.'''

#usando for
'''soma = 0
for i in range(1,500,1):
    if i%2!=0 and i%3==0:
        soma = soma + i
print(soma)'''

#usando while
i=1
soma =0
while i!=500:
    if i%2!=0 and i%3==0:
        soma +=i
    i+=1
print(soma)
        
    
    

