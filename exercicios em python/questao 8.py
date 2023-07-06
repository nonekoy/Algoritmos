mes= ['(1) Janeiro', '(2) Fevereiro', '(3) Março', '(4) Abril','(5) Maio', '(6) Junho', '(7) Julho', '(8) Agosto', '(9) Setembro', '(10) Outubro', '(11) Novembro', '(12) Dezembro']
temp= []
i= int

for i in range(12):
    print('Diga a temperatura média do mês de', mes[i])
    temp.append(float(input()))
media= sum(temp)/len(temp)
print('A temperatura média do ano é', '%2.1f'%media)
Alta= []
for i in range(12):
    if temp[i] >= media:
        Alta.append(temp[i])
    else:
        Alta.append('abaixo')

for i in range(12):
    print(mes[i], ' '*(17 -(len(mes[i]))), '=>', Alta[i])