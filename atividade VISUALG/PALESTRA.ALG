Algoritmo "palestra"
Var
   nome : caractere
   idade : inteiro
   Nota : caractere
   Na, Nb, Nc, Nd, Ne : inteiro
   Cont : inteiro
   somaidade, media : real
Inicio

   para Cont de 1 at� 20 passo 1  faca
      escreva ("diga o seu nome :")
      leia (Nome)
      escreva ("digite sua idade:")
      leia (idade)
      escreval ("d� uma nota para a palestra de A at� E,")
      escreva ("sendo 'A' muito bom e 'E' muito ruim:")
      leia(nota)
      se nota = "A" entao
         Na := Na + 1
      fimse
      se nota = "B" entao
         Nb := Nb + 1
      fimse
      se nota = "C" entao
         Nc := Nc + 1
      fimse
      se nota = "D" entao
         Nd := Nd + +1
      fimse
      se nota = "E" entao
         Ne := Ne + 1
      fimse
      somaidade := somaidade + idade
      escreval(" ")
   fimpara
   media := somaidade / Cont

   escreva("Notas A:", Na, ". ")
   escreva("Notas B:", Nb, ". ")
   escreva("Notas C:", Nc, ". ")
   escreva("Notas D:", Nd, ". ")
   escreval("Notas E:", Ne, ".")
   escreva("A idade m�dia dos alunos � de:", media)

Fimalgoritmo