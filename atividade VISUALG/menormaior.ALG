Algoritmo "testepara"
Var
   Cont: inteiro
   x: inteiro
   ContN: inteiro
   ContM: inteiro

Inicio
   para Cont de 1 at� 10 passo 1 faca
      escreva("informe o valor n�mero", Cont, " :")
      leia(x)
      se Cont = 1 entao
         ContN := x
      fimse
      se (x > ContM) entao
         ContM := x
      fimse
      se (x < ContN )entao
         ContN := x
      fimse
   fimpara

   escreval("O menor n�mero �", ContN)
   escreval("O maior n�mero �", ContM)

Fimalgoritmo