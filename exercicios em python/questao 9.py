resposta= str
susp= int(0)
i= int
pergunta=['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Tinha dívidas com a vítima?', 'Já trabalhou com a vítima?']

print('Questionário para o investigado:')
for i in range(5):
    print(pergunta[i])
    resposta= input()
    if resposta== 'sim' or resposta == 's':
        susp += 1
    else:
        susp += 0
if susp== 5:
    print('O entrevistado provavelmente é culpado.')
elif susp == 3 or susp ==4:
    print('O entrevistado provavelmente é cúmplice.')
elif susp == 2:
    print('O entrevistado é suspeito.')
else:
    print('O entrevistado é inocente.')
