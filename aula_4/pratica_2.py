soma_par = 0
A = int(input('Número inicial: '))
B = int(input('Número final: '))

for i in range(A, B+1, 1):
    if i % 2 == 0:
        soma_par += i
if A > B:
    for i in range(B, A + 1, 1):
        if i % 2 == 0:
            soma_par += i
        
print(f'Soma: {soma_par}')