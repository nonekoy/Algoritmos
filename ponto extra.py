#Grupo= João Vitor Freire, Natan Gabriel, Vinícius de Carvalho
Selec= int(input((('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
'Diga a operação desejada:\n'
'1 - Cadastrar produto\n'
'2 - Alterar produto\n'
'3 - Listar e contar produto\n'
'4 - Deletar produto\n'
'5 - Finalizar programa\n'
'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
'Sua escolha é: '
))))

cont= int(1)
sn= bool(True)
resposta= str
i = int
lista = []

while Selec >=0:
    if Selec == 1:
        while sn==True:
            produto=input('Digite o produto deseja adicionar: ')
            lista.append(produto)
            resposta = input('Deseja adicionar algo mais? sim ou não: ')
            if resposta== 'sim' or resposta== 's':
                sn= True
            else:
                sn = False
        sn = True
        print ("\n" * 130)
    
    elif Selec == 2:
        if lista==[]:
            print ("\n" * 130)
            print('Não há nenhum produto na lista ainda.')
        else:
            print ("\n" * 130)
            print('Deseja alterar qual produto?')
            i = 1
            contl = 1
            for i in lista:
                print(contl, '-', i)
                contl= contl + 1
            i = int(input('digite o número do item: '))      
            if (i-1) <= (len(lista)-1):
                lista[i-1]= str(input('deseja modificar para o que?\n'))
                print ("\n" * 130)
                print('Produto modificado.')    
            else:
                print ("\n" * 130)
                print('Erro, nenhum produto selecionado.')
                
    elif Selec == 3:
        print ("\n" * 130) 
        if lista==[]:
            print('Não há nenhum produto na lista ainda.')
        else:
            print('Aqui está a lista de produtos adicionados:')
            i = 1
            contl = 1
            for i in lista:
                print(contl, '-', i)
                contl= contl + 1

    elif Selec == 4:
        if lista==[]:
            print ("\n" * 130)
            print('Não há nenhum produto na lista ainda.')
        else:
            print ("\n" * 130)
            print('Deseja deletar qual produto?')
            contl = 1
            for i in lista:
                print(contl, '-', i)
                contl= contl + 1
            i = int(input('Digite o nome do produto:  '))
            if i-1 > (len(lista)-1):
                print ("\n" * 130)
                print('Erro, nenhum produto selecionado.')
            else:
                lista.pop(i-1)
                print ("\n" * 130) 
                print('Produto deletado da lista.')

    else: 
        print ("\n" * 130)
        print('programa terminado.')
        exit()
    
    Selec=int(input((('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
    'Diga a operação desejada:\n'
    '1 - Cadastrar produto\n'
    '2 - Alterar produto\n'
    '3 - Listar e contar produto\n'
    '4 - Deletar produto\n'
    '5 - Finalizar programa\n'
    '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
    'Sua escolha é: \n'
    ))))
#paz