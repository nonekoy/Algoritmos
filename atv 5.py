Num1= float(input('Digite o primeiro número:'))
Num2= float(input('Digite o segundo número:'))

Fim= int(input('''Diga o tipo de operação que deseja pelo sinal:
 1(multiplicação), 2(divisão), 3(soma) e 4(subtração)
 '''))

if Fim == 1:
    Mult= Num1 * Num2
    print('A multiplicação dos termos', Num1, 'e', Num2, 'é:', Mult)
if Fim == 2:
    Div= Num1 / Num2
    print('A divisão entre os números', Num1, 'e', Num2, 'é:', Div)
if Fim == 3:
    Soma= Num1 + Num2
    print('A soma dos números', Num1, 'e', Num2, 'é:', Soma)
if Fim == 4:
    Sub= Num1 - Num2
    print('A subtração dos números', Num1, 'e', Num2, 'é', Sub)