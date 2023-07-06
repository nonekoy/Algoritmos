#Grupo Enzo Nonato, Natan Gabriel, Ricardo Porfírio, Vinícius de Carvalho
import os
from typing import Collection
Op= int
valorfinal= float
valorp= []
valor = []
y= str
from tkinter import *

def menu():
  texto= (((
  'Marcenaria do Natanzito\n'
  '1- Monte seu próprio móvel\n'
  '2- Escolha móveis prontos\n'
  '3- Lista de compras\n'
  '4- Remover móvel\n'
  '5- Finalizar pedido\n'
  '0- Cancelar e finalizar o programa\n')))
  textointerno['text'] =texto
  
  try:
    Op= int(input())
  except ValueError:
    Op = None
  if Op== None:
    None
  else:
    return Op

def moveis():
  os.system('cls')
  b = "opção inválida."
  texto=(((
                "-=-=-= Escolha o Móvel desejado -=-=-=\n"
                "1 - Mesa (2 Folha de madeira)\n"
                "2 - Armário (4 Folhas de madeira)\n"
                "3 - Cômoda (2 Folhas de madeira)\n"
                "4 - Cadeira (25% de Desconto)\n"
                "5 - Guarda-Roupa (5 Folhas de madeira)\n"
                "6 - Porta (2.5 Folhas de madeira)\n"
                "7 - Cama (3.5 Folhas de madeira)\n"
                "8 - Painel (3 Folhas de madeira)\n"
                "9 - Prateleira (50% de desconto)\n"
            )))
  texto()
  while b == "opção inválida.":
      a = int(input("Digite a opção desejada: "))
      y = 'ped.cod nu '
      if a == 1:
        b = 2
        y = y+'01'
      elif a == 2:
        b = 4
        y= y+'02'
      elif a == 3:
        b = 2
        y= y+'03'
      elif a == 4:
        b = 0.75
        y= y+'04'
      elif a == 5:
        b = 5
        y= y+'05'
      elif a == 6:
        b = 2.5
        y= y+'06'
      elif a == 7:
        b = 3.5
        y= y+'07'
      elif a == 8:
        b = 3
        y= y+'08'
      elif a == 9:
        b = 0.5
        y= y+'09'
      else:
        print("Opção inválida")
        b = "opção inválida."
  return b, y

def tipo_madeira(y):
    os.system('cls')
    b = "Opção inválida."
    texto=(((    "=-=- TIPOS DE MADEIRA =-=-\n"
                "\n"
                "1 - MDF: $ 900,00\n"
                "2 - MDP: $ 750,00\n"
                "3 - Compensado: $ 500,00\n"
                "4 - Mogno africano: $ 1.750,00\n"
                "5 - Cumaru: $ 1.500,00\n"
                "6 - Carvalho: $ 1.100,00\n"
            )))
    texto()
    while b == "Opção inválida.":
        b = float(input("Escolha a sua Madeira: "))
        if b == 1:
            z = 900
            y = y+'11'
        elif b == 2:
            z = 750
            y = y+'22'
        elif b == 3:
            z = 500
            y = y+'33'
        elif b == 4:
            z = 1750
            y = y+'44'
        elif b == 5:
            z = 1500
            y = y+'55'
        elif b == 6:
            z = 1100
            y = y+'66'
        else:
            print("Opção inválida.")
            b = "Opção inválida."
    return z, y

def tamanho(y):
    os.system('cls')
    a = "Opção inválida."
    texto=(((
                "1 - Duplo (Dobro do Preço)\n"
                "2 - Padrão (Preço Normal)\n"
                "3 - reduzido (25% De desconto)\n"
            )))
    texto()
    while a == "Opção inválida.":
        a = int(input("Digite o tamanho do móvel: "))
        if a == 1:
            z = 2
            y = y+'01'
        elif a == 2:
            z = 1
            y = y+'02'
        elif a == 3:
            z = 0.75
            y = y+'03'
        else:
            print("Opção inválida.")
            a = "Opção inválida."
    return z, y

def pront():
  os.system('cls')
  contl=int(1)
  prontos=[['Mesa', 350.00],['Armário', 430.00],['Cômoda', 240.00],['Cadeira', 79.99],['Guarda-roupa', 600.00],['Porta', 480.00],['Cama', 500.00],['Painel', 300.00],['Prateleira', 300.00]]
  texto=((('Aqui é uma lista de amostra de móveis já prontos no depósito:\n'
  '    Móvel          |  Preço')))
  texto()
  for i in prontos:
    cont= len(i[0])    
    print(contl,'-', i[0], ' ' * (16-cont),'R$', '%4.2f'%i[1])
    contl+= 1
  selec= int(input('Qual o móvel desejado?\n'))
  selec= selec -1
  if selec<= len(prontos):
    valorp = prontos[selec]
    os.system('cls')
    return valorp
  else:
    os.system('cls')
    print('valor não existente.')
  
def listartudo(valor):
  os.system('cls')
  texto=((('Aqui está a lista de móveis:\n'
  '   Móveis                  |  Preço')))
  texto()
  contl=int(0)
  total = float(0)
  for i in valor:
    cont = int(len(i[0]))
    contl= contl+1
    print(contl,'-',i[0],' ' * (23-cont),'R$', '%4.2f'%i[1])
    preco= i[1]
    total= preco + total
  print('                     TOTAL = R$', '%4.2f'%total)
  cancel= input('Aperte enter para retornar ao menu.')
  if cancel== 0:
    os.system('cls')
  else:
    os.system('cls')
    
def apagar(valor):
  os.system('cls')
  contl = int(0)
  total = float(0)
  texto=('Essa é a lista de compras atual:')
  texto()
  for i in valor:
    cont = int(len(i[0]))
    contl= contl+1
    print(contl,'-',i[0],' ' * (23-cont),'R$', '%4.2f'%i[1])
    preco= i[1]
    total= preco + total
  try:
    apague = int(input('Digite qual você deseja apagar:'))
    apague = apague - 1
    try:
      del valor[apague]
      os.system('cls')
      return valor
    except IndexError:
      os.system('cls')
      print('Não há produto com esse valor, tente novamente.')
  except ValueError:
    os.system('cls')
    print('valor inexistente.')
  
def finalizar(valor):
  os.system('cls')
  contl = int(0)
  total = float(0)
  texto=('A lista de compras foi:')
  texto()
  for i in valor:
    cont = int(len(i[0]))
    contl= contl+1
    print(contl,'-',i[0],' ' * (23-cont),'R$', '%4.2f'%i[1])
    preco= i[1]
    total= preco + total
  print('O valor total é: R$''%4.2f'%total)
  while True:
    viagem = int(input('Será necessário frete(taxa de R$90)? Digite 1 para sim e 2 para não'))
    if viagem ==1:
      total = total + 90
      print('O valor total é: R$''%4.2f'%total)
      break
    elif viagem ==2:
      break
    else: 
      print('Opção não existe.')
  while True:
    print('O pagamento será em (1)dinheiro, (2)cartão ou (3)pix?')
    pagam= int(input('Digite o número:'))
    if pagam == 1 or pagam == 2 or pagam ==3:
      break
    else:
      print('Opção não existente.')
  return 

def loop():
  
  while True:
    
    if Op == 1:
      multiplicador, y = moveis()
      preco_madeira, y = tipo_madeira(y)
      preco = preco_madeira * multiplicador
      metragem, y = tamanho(y)
      preco_final = preco * metragem
      valorp= [y, preco_final]
      valor.append(valorp)
      os.system('cls')
      print(f"Preço final do Produto: {preco_final}")

    elif Op == 2:
      os.system('cls')
      valorp = pront()
      if valorp != 0:
        valor.append(valorp)
      else:
        None
        
    elif Op == 3:
      if valor == [] or valor == None:
        os.system('cls')
        print('Não há nada na lista de compras ainda.')
      else:
        listartudo(valor)

    elif Op == 4:
      if valor == [] or valor == None:
        os.system('cls')
        print('A lista de compras ainda está vazia.')
      else:
        apagar(valor) 
      
    elif Op == 5:
      final = finalizar(valor)
      break

    elif Op == 0:
      os.system('cls')
      print('Operações canceladas, programa finalizado.')
      exit()
      
    else:
      os.system('cls')
      print('Opção selecionada não existe, tente novamente.')
  
  print('Muito obrigado pela preferência, volte sempre.')



window = Tk()
window.title('Marcenaria do Natanzito')

textomain= Label(window, text= 'Bem vindo')
textomain.grid(column=2, row=2)
janela= Label(window, text='')
janela.grid(column=2, row= 6)
textointerno= Frame(window, text='')
textointerno.grid(column= 2, row= 8)


window.mainloop()
#pás