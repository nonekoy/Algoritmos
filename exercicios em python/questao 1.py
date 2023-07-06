popA = 80000
popB = 200000
taxA = 1.03
taxB = 1.015
ano= int(1)
crescA= (ano*taxA)*popA + popA
crescB= (ano*taxB)*popB + popB
while crescA < crescB:
    print('No ano', ano, 'população A tem:', crescA, 'de habitantes.\n')
    print('já a população b tem:', crescB, 'no total de habitantes.\n')
    crescA= (ano*taxA)*crescA 
    crescB= (ano*taxB)*crescB 
    ano = ano +1
    print('\n')
print('levou', ano, 'anos para a população A ultrapassar a população B.')