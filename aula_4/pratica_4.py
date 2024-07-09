
vetor = []
for i in range(10):
    elemento = int(input())
    vetor.append(elemento)

print(vetor)
print('\nElementos pares:')
for i in vetor:
    if i%2==0:
        print(i)