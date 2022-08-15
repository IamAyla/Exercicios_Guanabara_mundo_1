#Um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e a qauntidade de anos. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário para ser aprovado.
valor_casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salário?'))
anos = int(input('Em quantos anos será o pagamento?'))

meses = anos * 12
parcela = valor_casa/meses
limite_parcela = salario * 0.3

if parcela > limite_parcela:
  print('Infelizmente seu empréstimo foi negado.')
else:
  print('Parabéns seu empréstimo foi aprovado! Serão {} parcelas no valor de {}.').format(meses, parcela)

#Um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão. -1 p/ binário -2 p/ octal -3 p/ hexadecimal
num = int(input('Digir um número inteiro: '))
print('''Escolha uma das bases para conversão
[1] para BINÁRIO
[2] para OCTAL
[3] para  HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
  print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
  print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
  print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else: 
  print('Opção inválida, tente novamente!')
  
#Escreva um programa que leia dois númeroos inteiros e compare-os, mostando na tela uma mensagem: O primeiro valor é maior; ou O segundo valor é maior; ou Não existe valor maior, os dois são iguais
n1 = int(input('Digit eum número:'))
n2 = int(input('Digite outro número:'))

if n1 == n2:
  print('Não existe valor maior, os dois são iguais')
elif n1 > n2:
  print('O primeiro valor é maior')
elif n2 > n1:
  print('O segundo valor é maior')
 
#Um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ela ainda vai se alistar ao serviço militar, Se é a hora de se alistar, Se já passou do tempo do alistamento, Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
ano_nasc = int(input('Que você nasceu?'))
ano_atual = int(input('Em que ano estamos?'))
tempo = ano_atual - ano_nasc

if tempo == 18:
  print('Chegou a hora de se alistar!')
elif tempo > 18:
  alist = tempo - 18
  print('Já passou sua hora de alistar... Passaram {} anos'.format(alist))
elif tempo < 18:
  blist = 18 - tempo
  print('Calma, sua hora chega em {} anos'.format(blist))
  
 #Crie um programa que leia as notas de um aluno e calcule a média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5: reprovado, Média entre 5 e 6.9: recuperação, Média 7 ou superior: aprovado
nota1 = float(input('Qual a nota na prova 1?'))
nota2 = float(input('Qual a nota na prova 2?'))

media = (nota1 + nota2)/2

if media < 5:
  print('Você foi reprovado! Sua média foi {}'.format(media))
elif media > 7: 
  print('Você foi aprovado e sua média foi {}'.format(media))
else:
  print('Você está de recuperação. Sua média '.format(media))
  
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua catergoria de acordo com a idade: Até 9 anos: Mirim, Até 14 anos: Infantil, Até 19 anos: Junior, Até 20 anos: Sênior, Acima: Master
ano_atual = 2022 
 #O ano deve ser atualizado se necessário

ano_nasc = int(input('Qual ano de nascimento do atleta? '))
idade = ano_atual - ano_nasc

if idade <= 9:
  print('Este atleta é da actegoria mirim')
elif 9 < idade <= 14:
  print('Este atleta é da categoria infantil')
elif 14 < idade <= 19:
  print('Este atleta é da categoria junior')
elif idade == 20:
  print('Este atleta é da categoria infantil')
else:
  print('Este atleta é da categoria sênior')
  
#Refaça o Desafio 035, acrescentado o recurso mostrar de mostrar que tipo de triângulo será formado: Equilátero: todos os lados iguais, Isósceles: dois lados iguais, Escaleno: todos os lados diferentes
a = int(input('Digite um lado: '))
b = int(input('Digite o outro lado: '))
c = int(input('Digite outro lado: '))

if a < b + c and b < a + c and c < a + b:
  print('Forma um triângulo!')
else:
  print('Não forma um triângulo!')

if a == b == c:
  print('Este triângulo é equilátero')
elif a == b or a ==c or b == c:
  print('Este triângulo é isósceles')
else:
  print('Este triângulo é escaleno')
  
#Desenvolva uma lógica que leia o peso e a ltura de uma pessoa, calcule seu IMC e mostre seu status.
peso = float(input('Digite seu peso: (kg)'))
altura = float(input('Digite sua altura: (m)'))

imc = peso/(altura*altura)

if imc < 18.5:
  print('Seu IMC é {}, isso quer dizer que você está abaixo do peso ideal'.format(imc))
elif 18.5 < imc < 25:
  print('Seu IMC é {}, isso quer dizer que você está no peso ideal'.format(imc))
elif 25 <= imc < 30:
  print('Seu IMC é {}, isso quer dizer que você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
  print('Seu IMC é {}, isso quer dizer que você está com obesidade'.format(imc))
elif imc > 40: 
  print('Seu IMC é {}, isso quer dizer que você está com obesidade morbida'.format(imc))
  
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: À Vista dinheiro/cheque: 10% de desconto, À vista no cartão: 5% de desconto, Em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS AYLA '))
preco = float(input('Qual o preço do produto?'))
print('As formas de pagamento são: à vista, cheque, cartão')
pag = int(input('''Qual a forma de pagamento?
[1] para à vista dinheiro/cheque
[2] para à vista no cartão
[3] para 2x no cartão
[4] para 3x ou mais no cartão 
'''))
if pag == 1:
  novo_preco = preco * 0.9
  print('Legal, conseguimos um desconto para você. O novo valor é R$ {}'.format(novo_preco))
elif pag == 2:
  novo_preco = preco * 0.95
  print('Legal, conseguimos um desconto para você. O novo valor é R$ {}'.format(novo_preco))
elif pag == 3:
  print('O valor da compra é R$ {}'.format(preco))
elif pag == 4:
  novo_preco = preco * 1.2
  print('O valor da compra terá um acréscimo devido ao juros e ficará em R$ {}'.format(novo_preco)) 
  
#Crie um programa que o computador jogar jokenpô com você
print('{:=^40}'.format(' JOKENPÔ '))

import random
jkp = ['pedra', 'papel', 'tesoura']
pc = (random.choice(jkp))

print('Me conta qual você escolheu, eu já escolhi o meu. Fica tranquilo que não vai mudar!')
escolha = int(input('''Qual você escolhe?
[1] pedra
[2] papel
[3] tesoura '''))

print('Eu escolhi {}!'.format(pc))

if pc == 'pedra' and escolha == 1:
  print('Empatamos!')
elif pc == 'pedra' and escolha == 2:
  print('Perdi :C')
elif pc == 'pedra' and escolha == 3:
  print('Ganhei :D')

elif pc == 'papel' and escolha == 1:
  print('Ganhei :D')
elif pc == 'papel' and escolha == 2: 
  print('Empatamos!')
elif pc == 'papel' and escolha == 3:
  print('Perdi :C')

elif pc == 'tesoura' and escolha == 1:
  print('Perdi :C')
elif pc == 'tesoura' and escolha == 2:
  print('Ganhei :D')
elif pc == 'tesoura' and escolha == 3:
   print('Empatamos!') 
    
#Faça um programa na tela que mostre na tela uma contagem regressiva para o estouro de fogod de artifício de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep
for n in range(10,-1,-1):
  print(n)
  sleep(1)
print('POW!')

#Crie um programa que mostre na tela todos os números pares que estão no intrevalo entre 1 e 50
for i in range(0,51,2):
  print(i)
  
#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram entre 1 até 500
for n in range(3,501,6):
  print(n)
  
#Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher utilizando o laço for.
n = int(input('Digite um número: '))
print('{:=^40}'.format(' TABUADA '))
print()
for a in range(1, 11,1):
  print('{} x {:2} = {}'.format(n,a, n*a))
  
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar desconsidere-o.
s = 0
for n in range(1,7):
  a = int(input('Digite o {}° número: '.format(n)))
  if a % 2 == 0:
    s += a
print(s)

#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão.
i = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = i + (10 - 1) * r

for pa in range(i,d,r):
  print('{}'.format(pa),end='->')
print('Acabou')

#Faça um programa que leia um número inteiro e diga se ele é um número primo
n = int(input('Digite seu número: '))
tot = 0
for a in range(1, n+1):
  if n % a == 0:
    tot += 1
print('O número {} foi  divisível {} vezes'.format(n, tot))
if tot == 2:
  print('Por isso ele é primo')
else:
  print('Ele não é primo')
  
#Crie um programa que leia um frase qualquer e diga se ela é um palíndromo, desconsiderando um os espaços.
frase = str(input('Digite sua frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
  inverso += junto[letra]
print('Você digitou a frase {}'.format(frase))
if inverso == junto:
  print('Temos um palíndromo!')
else:
  print('Não é um palíndromo!')
  
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores.
from datetime import date
atual = date.today().year
maior = 0
menor = 0

for pessoa in range (1,8):
  nasc = int(input('Em que ano a {}ª pessoa nasceu?'.format(pessoa)))
  idade = atual - nasc
  if idade>= 21:
      maior += 1
  else:
     menor += 1

print('No total tivemos {} maiores e {} menores'.format(maior, menor))

#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso.
maior = 0
menor = 0

for pessoa in range (1,6):
  peso = float(input('Qual o peso da {}ª pessoa?'.format(pessoa)))
  if pessoa == 1:
    maior = peso
    menor= peso
  else:
    if peso > maior:
      maior = peso
    if peso < maior:
      menor = peso

print('O maior peso lido foi de  {}kg e o menor foi {}kg'.format(maior, menor))

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.No final do programa, mostre: A média de idade do grupo, O nome do homem mais velho, A quantidade de mulheres que tem menos de 20 anos
soma = 0
velhohomem = 0
nomevelho = ''
totm = 0

for p in range(1,5):
  print('{:-^40}'.format(' {}ª pessoa '.format(p)))
  nome = str(input('Nome: '))
  idade = int(input('Idade: '))
  sexo = str(input('Sexo: [M/F] '))
  soma += idade
  if p == 1 and sexo in 'Mm':
    velhohomem = idade
    nomevelho = nome
  if sexo in 'Mm' and idade > velhohomem:
    velhohomem: idade
    nomevelho = nome
  if sexo in 'Ff'and idade < 20:
    totm += 1


media = soma / 4 

print('A média de idade do grupo é de {} anos, o homem mais velho é {} e a quantidade de mulheres com menos de 20 anos é {}'.format(media, nomevelho,totm))

#Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto
sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
while sexo not in'FfMm':
  sexo = str(input('Dados inválidos. Digite seu sexo: [M/F] ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

#Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10. Só que o jogador vai tentar até acertar, mostrando no final a quantidade de palpites que foram necessários para vencer
acertou = False
palpite = 0
print('Vou escolher um número entre 0 e 10 e você precisa advinhar')

print('Hum, vamos ver...')
from random import randint
pc = randint(0, 10)
from time import sleep
sleep(3)
print('Já escolhi')

while not acertou:
  r = int(input('Advinha: '))
  if  r == pc:
    acertou = True
    palpite += 1
  else: 
    if r < pc: 
      print('Mais... Tenta de novo')
    elif r > pc:
      print('Menos... Tenta de novo')
print('Acertou! Com {} tentativas'.format(palpite))

#Crie um programa que leia dois valores e mostre um menu na tela: [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep
opcao = 0
print('=-='*10)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
print('=-='*10)

while opcao != 5:
  print('''
  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair do programa''')
  print('=-='*10)
  opcao = int(input('O que você quer fazer? '))

  if opcao == 1:
    soma = n1 + n2
    print('A soma é {}'.format(soma))
  elif opcao == 2:
    mult = n1 *  n2
    print('O produto é {}'.format(mult))
  elif opcao == 3:
    if n1 > n2:
      print('{} é maior que {}'.format(n1, n2))
    elif n2 > n1:
        print('{} é maior que {}'.format(n2, n1))
    else:
      print('Os números são iguais')
  elif opcao == 4:
    print('Informe os números novamente: ')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
  elif opcao == 5:
    print('Finalizando...')

  else:
    print('Opção inválida. Tente novamente.')
sleep(2)
print('Fim do programa!')

#Faça um programa que leia um número qualquer e mostre o seu fatorial
f = int(input('Digite um número para calcular seu fatorial: '))
c = f
fat = 1
while c > 0:
  print('{}'.format(c), end = '')
  print(' x ' if c > 1 else ' = ', end = '')
  fat *= c
  c -= 1
  
print('{}'.format(fat))

#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão com a estrutura while
print('{:=^40}'.format(' GERADOR DE PA '))

p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p
cont = 1
while cont <= 10:
  print('{} -> '.format(termo),  end = '')
  termo += r
  cont += 1
print('FIM!')

#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print('{:=^40}'.format(' GERADOR DE PA '))

p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p
cont = 1
total = 0
t2 = 10
while t2 != 0:
  total += t2
  while cont <= total:
    print('{} -> '.format(termo),  end = '')
    termo += r
    cont += 1
  print('PAUSA')
  t2 = int(input('Quantos termos quer mostrar a mais? '))
print('FIM!')

#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci
print('=-='*10)
print('Sequência de Fibonacci')
print('=-='*10)

n = int(input('Digite o número de termos: '))

t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end = '')

cont = 3
while cont <= n:
  t3 = t1 + t2
  print('-> {}'.format(t3), end = '')
  cont += 1
  t1 = t2
  t2 = t3
print(' -> FIM')

#Crie um porgrama que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. no final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
num = cont = s = 0
num = int(input('Digite um número inteiro [999 para parar]: '))
while num != 999:
  cont += 1
  s += num
  num = int(input('Digite um número inteiro [999 para parar]: '))

print('Você digitou {} números e a soma foi {}'.format(cont, s))
print('Acabou!')

#Crie um programa que leia vários números inteiros pelo teclado. No final mostre a média entre todos os valores e qual foi o maior e menor valor lido. O porgrama deve perguntar ao usuário se ele quer ou não continuar a digitar valores
resp = 'S'
soma = media = quant = maior = menor = 0

while resp in 'S':
  num = int(input('Digite um número: '))
  soma += num
  quant += 1
  if quant ==1:
    maior = menor = num 
  else:
    if num > maior:
      maior = num
    elif num < menor:
      menor = num
    
  resp = str(input('Quer continar: [S/N]')).upper().strip()[0]

media = soma/quant

print('Você digitou {} números e a média foi {}. O maior foi {} e o menor foi {}'.format(quant, media, maior, menor))

#Crie um programa que leia vários números inteiros pelo teclado. O programa só ai parar quando o usuário digitar o valor 999, que a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
s = c = 0
while True:
  n = int(input('Digite um número (999 para parar): '))
  if n == 999:
    break
  c += 1
  s += n

print(f'Você digitou {c} valores e a soma deles foi {s}'
     
#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('{:=^40}'.format(' GERADOR DE TABUADA '))

while True:
  n = int(input('Quer ver a tabuada de que valor? '))
  print('=-='*10)
  if n < 0:
    break
  for a in range(1, 11,1):
    print('{} x {:2} = {}'.format(n,a, n*a))
  print('=-='*10)
print('Programa encerrado!')
      
#Faça um programa que jogue par ou ímpar para o computador. O jogo só será interrompido se o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
print('=-='*10)
print('Vamos jogar par ou ímpar?')
print('=-='*10)

while True:
  n = int(input('Diga um valor: '))
  escolha = str(input('PAR ou ÍMPAR? [P/I]')).upper()
  from random import randint
  pc = randint(0, 1000)
  s = n + pc
  if s % 2 == 0 and escolha in 'P':
      print(f'Eu escolhi {pc}')
      print('Você ganhou!')
      print('Vamos de novo...')
      print('=-='*10)
  elif s % 2 != 0 and escolha in 'I':
      print(f'Eu escolhi {pc}')
      print('Você ganhou!')
      print('Vamos de novo...')
      print('=-='*10)
  else:
    break
print('=-='*10)
print(f'Eu escolhi {pc}')
print('Fim do jogo! Você perdeu :P')
   
#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: a) quantas pessoas tem mais de 18 anos; b) quantos homens foram cadastrados; c) quantas mulheres tem menos de 20 anos;
maior18 = homens = menor20 = 0

while True:
  print('-'*30)
  print('CADASTRE UMA PESSOA')
  print('-'*30)
  idade = int(input('Idade: '))
  sexo = str(input('Sexo: ')).upper().strip()[0]
  while sexo not in'FfMm':
    sexo = str(input('Dados inválidos. Sexo: [M/F] ')).upper().strip()[0]
  print('-'*30)

  if idade > 18:
    maior18 += 1
  if sexo == 'M':
    homens += 1
  if idade < 20 and sexo == 'F':
    menor20 += 1


  seguir = str(input('Quer continuar? [S/N]')).upper()
  while seguir not in'SsNn':
    seguir = str(input('Dados inválidos. Quer continuar? [S/N] ')).upper()

  if seguir == 'N':
    break

print(f'Existem {maior18} maiores de 18 anos')
print(f'Há {homens} homens cadastrados')
print(f'E há {menor20} mulheres com menos de 20 anos')
print('{:=^40}'.format(' FIM DO PROGRAMA '))
      
#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: a) Qual é o total gasto na compra? b) Quantos produtos custam mais de R$ 1000? c) Qual é o nome do produto mais barato?
print('-'*30)
print('{:^30}'.format('ATACADÃO DA AYLA'))
print('-'*30)

total = caro = menor = cont = 0 
barato = ''

while True:
  produto = str(input('Nome do produto: '))
  preco = int(input('Preço: R$ '))
  cont += 1
  total += preco
  if preco > 1000:
      caro += preco
  if cont == 1 or preco < menor:
    menor = preco
    barato = produto

  seguir = str(input('Quer continuar? [S/N]')).upper()
  while seguir not in'SsNn':
      seguir = str(input('Dados inválidos. Quer continuar? [S/N] ')).upper()
  print('-'*30)
  if seguir == 'N':
      break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
      
#Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Obs: Considere que o caixa possui cédulas de 50, 20, 10 e 5
print('='*30)
print('{:^30}'.format('BANCO DA AYLA'))
print('='*30)

valor = int(input('Qual o valor do saque? R$ '))
total = valor 
ced = 50
totalced = 0

while True:
  if total >= ced:
    total -= ced
    totalced += 1
  else:
    if totalced > 0:
      print(f'Total de {totalced} cédulas de R$ {ced}')
    if ced == 50:
      ced == 20
    elif ced == 20:
      ced == 10
    elif ced == 10:
      ced == 1
    totalced = 0
    if total == 0:
      break


print('='*30)
print('Volte sempre! Tenha um bom dia!')
