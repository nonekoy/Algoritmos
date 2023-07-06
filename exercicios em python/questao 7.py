ListaNota= []
nota= float(0)
i= int
cont= int

while True:
    print('Diga a nota do aluno')
    nota= float(input())
    if nota >=0:
        ListaNota.append(nota)
    else:
        break
print('Foram adcionadas', len(ListaNota), 'notas.')

print('A lista de notas foi:')
for i in range((len(ListaNota))):
    print(ListaNota[i])

ListaNota.reverse()
print('O inverso da lista é:')
for i in range(len(ListaNota)):
    print(ListaNota[i])

print('A soma das notas é', sum(ListaNota), '.')
media = sum(ListaNota)/len(ListaNota)
print('A média das notas é', media,'.')
print('As notas acima da média são:')

for i in range(len(ListaNota)):
    if ListaNota[i]>= media:
        print(ListaNota[i])
