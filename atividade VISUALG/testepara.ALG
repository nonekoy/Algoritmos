Algoritmo "testepara"
Var
Cont: inteiro
x: real
ContI: inteiro
ContP: inteiro


Inicio

para Cont de 1 at� 10 passo 1 faca
escreva("informe o valor n�mero", Cont, " :")
leia(x)
se (x mod 2 = 0) entao
  ContP := ContP + 1
  senao
  ContI := ContI + 1
fimse
fimpara

escreval("Aqui tem", ContP, " n�meros pares.")
escreval("e tamb�m", ContI, " n�meros �mpares.")

Fimalgoritmo