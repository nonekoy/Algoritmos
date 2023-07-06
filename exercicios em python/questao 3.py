candA= int(0)
candB= int(0)
candC= int(0)
voto= int(0)
i = int
for i in range(20):
    print((('Digite o número do partido do seu candidato:\n'
    'Candidato A ---- Partido 88\n'
    'Candidato B ---- Partido 51\n'
    'Candidato C ---- Partido 39\n'
    'Diga o seu voto:'
    )))
    voto = int(input())
    if voto == 88:
        candA= candA + 1
        print('você votou no candidato A')
    elif voto == 51:
        candB= candB + 1
        print('você votou no candidato B')
    elif voto == 39:
        candC = candC + 1
        print('você votou no candidato C')
    else:
        print('voto nulo ou em branco')

if candA > candB and candA > candC:
    print('O candidato A venceu!')
elif candB > candA and candB > candC:
    print('O candidato B venceu!')
elif candC > candA and candC > candB:
    print('O candidato C venceu!')
else:
    print('A eleição não pôde ocorrer.')