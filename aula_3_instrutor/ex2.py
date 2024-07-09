valor_emprestimo = float(input('Valor do empréstimo: '))
n_parcelas = int(input('Parcelas: '))
salario_solicitante = float(input('Salário do solicitante: '))

if (valor_emprestimo/n_parcelas) <= salario_solicitante*0.3:
    print(f'Parcela: {valor_emprestimo/n_parcelas:.2f}')
    print(f'30% salario: { salario_solicitante*0.3}')
    print('Aprovado')
else:
    print('Ganhe mais dinheiro')
    print(f'Parcela: {valor_emprestimo/n_parcelas:.2f}')
    print(f'30% salario: { salario_solicitante*0.3}')