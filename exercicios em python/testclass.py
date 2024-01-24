
class elevador:
    peso= float
    andares= [1, 2, 3, 4, 5, 6]
    def pesomax(peso,y):
        max = peso+ y
        if max <= 1000:
            print("funcionando normalmente.")
        else:
            print("por favor, retire peso do elevador.")
    
def andar(piso):
    print("defina o andar atual:")
    try:
        andaratual = int(input)
        print("indo ao andar ",andaratual)
        andaratual= andaratual-1
    except (andaratual> len.andares+1)|(andaratual<1):
        print("andar não existente.")
        print("ainda no andar ",andaratual)
    
class andares:
    andar= ["terreo", "1º", "2º","3º","4º","5º"]
    def aqui(n):
        print("você está no andar: ",andar[n-1])

    