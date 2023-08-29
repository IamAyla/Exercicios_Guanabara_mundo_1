#Um título bonitinho
print('{:=^40}'.format(' JOKENPÔ '))

#Importando a biblioteca a ser utilizada, definindo a lista e deixando o PC escolher
import random
jkp = ['pedra', 'papel', 'tesoura']
pc = (random.choice(jkp))

#Recebendo a escolha do jogador
print('Me conta qual você escolheu, eu já escolhi o meu. Fica tranquilo que não vai mudar!')
escolha = int(input('''Qual você escolhe?
[1] pedra
[2] papel
[3] tesoura '''))

#cContando a escolha para o jogador
print('Eu escolhi {}!'.format(pc))

#Se o PC escolhe pedra, resultados
if pc == 'pedra' and escolha == 1:
  print('Empatamos!')
elif pc == 'pedra' and escolha == 2:
  print('Perdi :C')
elif pc == 'pedra' and escolha == 3:
  print('Ganhei :D')
  
#Se o PC escolhe papel, resultados
elif pc == 'papel' and escolha == 1:
  print('Ganhei :D')
elif pc == 'papel' and escolha == 2: 
  print('Empatamos!')
elif pc == 'papel' and escolha == 3:
  print('Perdi :C')

 #Se o PC escolhe tesoura, resultados
elif pc == 'tesoura' and escolha == 1:
  print('Perdi :C')
elif pc == 'tesoura' and escolha == 2:
  print('Ganhei :D')
elif pc == 'tesoura' and escolha == 3:
   print('Empatamos!') 
