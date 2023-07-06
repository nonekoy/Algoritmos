i = int(1)
x = float
y = []
num = float
par = int(0)
impar = int(0)
for i in range(10):
    print('digite o', i + 1 , 'º número:')
    num = float(input())
    y.append(num)
    if num % 3 == 0:
        par= par + 1
    else:
        impar= impar + 1
print('na lista de números:\n')
for i in y:
    print('%.d' %(i))
print(par, 'são números pares, e', impar,'são números ímpares.')
