media = float(0)
quant = int(0)
mais= bool(True)
resp = str

while mais == True:
    idade= int(input('Diga a sua idade:'))
    media= media + idade
    quant += 1
    resp = (input('Deseja adicionar mais alguém? (sim ou não?) :'))
    if resp == 'sim' or resp == 's':
        mais = True
    else:
        mais = False

final = media/quant

if final < 25:
    print('Essa turma é jovem ainda.')
elif final >= 26 and final <= 60:
    print('Essa turma é adulta.')
elif final >60:
    print('Essa turma é idosa.')