#ler ano de nascimento e escrever se pode votar ou não

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = 2024 - ano_nascimento 
if(idade>=18):
    print('Voto Obrigatório')
else:
    print('Você não precisa votar esse ano')