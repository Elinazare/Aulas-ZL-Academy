'''Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão para o 
garçom. Fazer um algoritmo que leia o valor gasto com despesas realizadas em um restaurante e imprima o 
valor total com a gorjeta.'''

valor_comanda = float(input('Digite o valor da comanda: '))
valor_total = valor_comanda + valor_comanda/10
print(f"O valor total com a gorgeta é: {valor_total}")