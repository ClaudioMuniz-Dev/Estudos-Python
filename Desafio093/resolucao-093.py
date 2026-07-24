lista = {}
gols = []
while True:
    nome = input('Nome do Jogador: ').strip()
    if nome.replace(' ','').isalpha():
        lista['nome'] = nome
        break
    else:
        print('Digite apenas o nome do jogador sem números ou caracteres especiais!')
while True:
    try:
        partidas = int(input(f'Quantas partidas {nome} jogou? '))
        break
    except ValueError:
        print('Erro, digite apenas números sem caracteres especiais!')
for c in range(partidas):
    while True:
        try:
            user = int(input(f'Quantos gols na partida {c}? '))
            gols.append(user)
            break
        except ValueError:
            print('Erro, digite apenas números sem caracteres especiais!')
lista['gols'] = gols
lista['total'] = sum(gols)
print('-=' *30)
print(lista)
print('-=' *30)
for k, v in lista.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' *30)
print(f'O jogador {nome} jogou {partidas} partidas.')
for c, g in enumerate(gols):
    print(f'   => Na partida {c}, fez {g} gols.')
print(f'Foi um total de {sum(gols)} gols.')
