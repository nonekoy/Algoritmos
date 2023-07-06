i = int(1)
o= int(1)
primos= []
p = int(2)
y= int
check= int
mult = int(0)
x = int(input('diga até que número quer checar os primos:'))

while (p + 1 != x):
    while i<= p or mult< 2:
        i = i + 1
        check= p % i
        if check== 0:
            mult = mult + 1
            
    if mult <= 2:
        primos.append(input(p))
    p = p + 1        

print('Os números primos são:')
for o in primos:
    print(o)