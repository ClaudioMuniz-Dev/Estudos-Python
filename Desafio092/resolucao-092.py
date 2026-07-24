from datetime import datetime
cadastro = dict()
ano_atual = datetime.now().year
while True:
    nome = input('Nome: ').strip()
    if nome.replace(' ', '').isalpha():
        cadastro['nome'] = nome
        break
    print('Erro: Digite apenas o nome sem números ou caracteres especiais!')
while True:
    try:
        nascimento = int(input('Ano de nascimento: '))
        cadastro['idade'] = ano_atual - nascimento
        break
    except ValueError:
        print('Erro: Digite apenas números inteiros!')
while True:
    try:
        cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
        break
    except ValueError:
        print('Erro: Digite apenas números inteiros!')
if cadastro['ctps'] != 0:
    while True:
        try:
            cadastro['contratação'] = int(input('Ano de contratação: '))
            break
        except ValueError:
            print('Erro: Digite apenas números inteiros!')
    while True:
        try:
            cadastro['salário'] = float(input('Salário: R$ '))
            break
        except ValueError:
            print('Erro: Digite apenas números válidos (use "." para decimais)!')
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - ano_atual)
print('-=' * 30)
for k, v in cadastro.items():
    print(f'  - {k.title()} tem o valor: {v}')
