#Mostrar a qtde total arrecadada nas vendas e mostrar 10% do valor a se guardar na poupança

pao = int(input('Digite a qtde de pães vendidos: '))
broa = int(input('Digite a qtde de broas vendidas: '))
total = pao*0.12 + broa*1.5
print(f'Você arrecadou {pao*0.12} reais  em  pães e {broa*1.5} reais em broa. Total: {total}')
print(f'Valor a ser guardado na poupança: {total*0.1}')