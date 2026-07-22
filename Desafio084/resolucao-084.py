pessoas=list()
dados=list()
mais_pesados=list()
mais_leves=list()
maior=menor=quantidade=0
while True:
    dados.append(input('Nome: '))
    while True:
        try:
            dados.append(float(input('Peso: ')))
            break
        except ValueError:
            print('Digite apenas números!')
            continue
    if quantidade==0:
        maior=dados[1]
        mais_pesados.append(dados[0])
        menor=dados[1]
        mais_leves.append(dados[0])
    else:
        if dados[1]==maior:
            mais_pesados.append(dados[0])
        elif dados[1]==menor:
            mais_leves.append(dados[0])
        elif dados[1]>maior:
            maior=dados[1]
            mais_pesados.clear()
            mais_pesados.append(dados[0])
        elif dados[1]<menor:
            menor=dados[1]
            mais_leves.clear()
            mais_leves.append(dados[0])
    pessoas.append(dados[:])
    quantidade+=1
    dados.clear()
    pergunta=input('Quer continuar? [S/N]: ').upper()
    if pergunta =='N':
        break
    while pergunta not in('S','N'):
        print('Por favor digite apenas as opções S ou N')
        pergunta = input('Quer continuar? [S/N]: ').upper()
if len(pessoas)==1:
    print('Ao todo você cadastrou 1 pessoa')
else:
    print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
if quantidade==1:
    print(f'O maior e menor peso ({maior}Kg) são de {mais_pesados}')
else:
    print(f'O maior peso foi de {maior}Kg. Peso de {mais_pesados}')
    print(f'O menor peso foi de {menor}Kg. Peso de {mais_leves}')
