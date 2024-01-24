cpd= int(input('Diga quantos cigarros por dia a pessoa fumou:'))
anos= int(input('Por quantos anos ela fumou:'))
cigto= cpd*(anos*365) #cigarros totais
perdeu= cigto * 10 #10 minutos perdidos por cigarro
diasp = perdeu/1440
print('No final essa pessoa perdeu', diasp,'dias de vida.')