Algoritmo "testepara"
Var
   Cont: inteiro
   x: inteiro
   ContN: inteiro
   ContM: inteiro

Inicio
   para Cont de 1 até 10 passo 1 faca
      escreva("informe o valor número", Cont, " :")
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

   escreval("O menor número é", ContN)
   escreval("O maior número é", ContM)

Fimalgoritmo