def resultado(roda, peso, pessoa):
    if (roda < 4):
        return "Categoria A."
    else :
        if (pessoa > 8):
            return "Categoria D."
        else: 
            if (peso< 3500):
                return "Categoria B."
            elif (peso>= 3500 and peso <6000):
                return "Categoria C."
            else:
                return "Categoria E."
    return "Erro de classificação"

print("Aqui iremos classificar qual carteira será necessária pelo seu veículo")
rodas = int(input("Diga a quantidade de rodas: "))
pesov = float(input("Diga o peso do veículo: "))
pessoas = int(input("Diga a quantidade máxima de pessoas no veículo: "))

print("Você precisa de uma carteira de", resultado(rodas, pesov, pessoas))