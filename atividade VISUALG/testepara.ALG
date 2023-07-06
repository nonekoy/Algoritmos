Algoritmo "testepara"
Var
Cont: inteiro
x: real
ContI: inteiro
ContP: inteiro


Inicio

para Cont de 1 até 10 passo 1 faca
escreva("informe o valor número", Cont, " :")
leia(x)
se (x mod 2 = 0) entao
  ContP := ContP + 1
  senao
  ContI := ContI + 1
fimse
fimpara

escreval("Aqui tem", ContP, " números pares.")
escreval("e também", ContI, " números ímpares.")

Fimalgoritmo