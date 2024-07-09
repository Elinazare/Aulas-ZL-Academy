salario = float(input())
tempo_serviço = int(input())

if tempo_serviço>=5:
    print(f'O salario com bônus é {salario*1.2:.2f}')
else:
    novo_salario = salario + salario*0.1
    print(f'O salario com bônus é {salario*1.1:.2f}')
  
