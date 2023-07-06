score= []
i = int
pontos= []

print('Qual o resultado das suas 10 partidas?')
print('para vitória use(v), derrota use(d) e empate use(e).')
for i in range(10):
    print('Diga o resultado da', i+ 1, 'partida:')
    score= str(input())
    if score=='v':
        pontos.append(10)
    elif score=='d':
        pontos.append(-2)
    elif score=='e':
        pontos.append(5)
    else:
        print('resposta não aceita.')
        exit()
        
print('|',pontos[0],'|',pontos[1],'|',pontos[2],'|',pontos[3],'|',pontos[4],'|',pontos[5],'|',pontos[6],'|',pontos[7],'|',pontos[8],'|',pontos[9],'| total=', sum(pontos),'|')


if sum(pontos) >= 60:
    print('Você foi promovido!')
elif sum(pontos)>= 21 and sum(pontos) <60:
    print('Você continuou na mesma patente.')
else:
    print('Você caiu de patente.')
