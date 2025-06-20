#variaveis

casa1_Grifinoria = 0
casa2_Corvinal = 0
casa3_LufaLufa = 0
casa4_Sonserina = 0

#pergunta1

pergunta1 = int(input("Q1)Se você estivesse em Hogwarts, como enfrentaria um desafio inesperado?  1) Com coragem e determinação  2) Com inteligência e estratégia "))

while pergunta1 != 1 and pergunta1 != 2:
  pergunta1 = int(input("Opção invalida so existem as opções 1 e 2 tente novamente: "))

#condição1
if pergunta1 == 1:
  casa1_Grifinoria += 1
  casa2_Corvinal += 1
  print("Ok Proxima pergunta")
elif pergunta1 == 2:
  casa3_LufaLufa += 1
  casa4_Sonserina += 1
  print("Ok Proxima pergunta")
else:
  print("Não existe essa opção retorne a mesnsagem")

#pergunta2

pergunta2 = int(input("Q2)Qual dessas qualidades de bruxo você mais admira?  1) Lealdade e justiça  2) Ambição e liderança  3) Inteligência e criatividade  4) Coragem e ousadia"))

while pergunta2 != 1 and pergunta2 != 2 and pergunta2 != 3 and pergunta2 != 4:
  pergunta2 = int(input("Opção invalida so existem as opções 1, 2, 3 e 4 tente novamente: "))


#condição2
if pergunta2 == 1:
   casa3_LufaLufa += 2
   print("Ok Proxima pergunta")
elif pergunta2 == 2:
   casa4_Sonserina += 2
   print("Ok Proxima pergunta")
elif pergunta2 == 3:
   casa2_Corvinal += 2
   print("Ok Proxima pergunta")
elif pergunta2 == 4:
   casa1_Grifinoria += 2
   print("Ok Proxima pergunta")
else:
   print("Não existe essa opção retorne a mesnsagem")

#pergunta3

pergunta3 = int(input("Q3)Se recebesse uma relíquia mágica rara, o que faria?  1) A usaria para proteger aqueles que ama  2) A estudaria para entender seu potencial  3) A esconderia para que ninguém abusasse dela  4) A usaria para alcançar seus próprios objetivos "))

while pergunta3 != 1 and pergunta3 != 2 and pergunta3 != 3 and pergunta3 != 4:
  pergunta3 = int(input("Opção invalida so existem as opções 1, 2, 3 e 4 tente novamente: "))

#condição3
if pergunta3 == 1:
  casa4_Sonserina += 4
elif pergunta3 == 2:
  casa3_LufaLufa += 4
elif pergunta3 == 3:
  casa2_Corvinal += 4
elif pergunta3 == 4:
  casa1_Grifinoria += 4
else:
  print("Não existe essa opção retorne a mesnsagem")

# Momento de descobrir qual casa voce pertence

if casa2_Corvinal > casa1_Grifinoria and casa2_Corvinal > casa3_LufaLufa and casa2_Corvinal > casa4_Sonserina:
  print("Voce pertence a casa Corvinal")
elif  casa3_LufaLufa > casa2_Corvinal and casa3_LufaLufa > casa1_Grifinoria and casa3_LufaLufa > casa4_Sonserina:
  print("Voce pertence a casa Lufa-lufa")
elif  casa1_Grifinoria > casa2_Corvinal and casa1_Grifinoria > casa3_LufaLufa and casa1_Grifinoria > casa4_Sonserina:
  print("Voce pertence a casa Grifinoria")
elif  casa4_Sonserina > casa2_Corvinal and casa4_Sonserina > casa3_LufaLufa and casa4_Sonserina > casa1_Grifinoria:
  print("Voce pertence a casa Sonserina")
else:
  ("Você não pertence a nenhuma casa")

fim = input("presione enter para fechar")