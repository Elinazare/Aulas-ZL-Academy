a = int(input('número 1: '))
b = int(input('número 2: '))
c = int(input('número 3: '))

if(a>b and a>c):
    print(a)
elif(b>c and b>a):
    print(b)
else:
    print(c)