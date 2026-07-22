from random import randint
from time import sleep
from operator import itemgetter
jogo=dict()
for c in range(1,5):
    jogo[f'jogador{c}'] = randint(1,6)
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores:')
for c, (k,v) in enumerate(sorted(jogo.items(), key=itemgetter(1), reverse=True),start=1):
    print(f'{c}º lugar: {k} com {v}')
    sleep(1)
