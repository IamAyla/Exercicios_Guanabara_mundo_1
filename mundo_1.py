#Criando um programa que leia dois números e leia a soma entre eles
n1 =int(input('Digite um número:'))
n2 =int(input('Digite mais um número:'))
s = n1 + n2

print('A soma vale', s)

#Fazendo um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as possíveis informações
x = (input('Digite algo:'))
print('O tipo primitivo é:{}'.format(type(x)))

print('É alfanumérico:', x.isalnum())
print('É alfabético:', x.isalpha())
print('É legível:', x.isascii())
print('É decimal:', x.isdecimal())
print('É número:', x.isnumeric())
print('É maiúsculo:', x.isupper())
print('É minúsculo:', x.islower())
print('Só tem espaço:', x.isspace())
print('É imprimível:', x.isprintable())
print('Está capitalizada:', x.istitle())

#Fazendo um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n = int(input('Diga um número:'))
a = n - 1
s = n + 1

print('A partir do valor de {}, temos que o antecessor é {} e o sucessor é {}'.format(n, a, s))

#Criando um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Diga um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro é {}, o triplo é {} e a raiz quadrada é {}'.format(d, t, r))

# Desenvolvendo um programa que leia duas notas de um aluno, calcule e mostre a média.
n = input('Qual o nome do aluno?')

p1 = float(input('Nota primeira prova:'))
p2 = float(input('Nota segunda prova:'))

m = (p1 + p2)/2

print('A média de {} é {}'.format(n, m))

#Escrevendo um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
v = float(input('Diga o valor em metros:'))

vc = v * 100
vm = v * 1000

print('{} metros representa: {} cm e {} mm'.format(v, vc, vm))

#Fazendo um programa que leia um número inteiro qualquer e mostre sua tabuada
n = int(input('Qual o número?'))

print('-'*12)
t1 = n * 1
t2 = n * 2
t3 = n * 3
t4 = n * 4 
t5 = n * 5 
t6 = n * 6
t7 = n * 7 
t8 = n * 8
t9 = n * 9
t10 = n * 10

print('A tabuada é: \n {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {} \n {} x 10 = {}'.format(n, t1, n, t2, n, t3, n, t4, n, t5, n, t6, n, t7, n, t8, n, t9, n, t10))
print('-'*12)

#Criando um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode gastar
r = float(input('Quantos reais você tem? R$'))

print('Então você tem {} dólares'.format(r/5.14))

#Fazendo um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta um parede de 2m²
a = float(input('Qual a altura?'))
l = float(input('Qual a largura?'))

print('A área é {}m², por isso, você vai precisar de {}l de tinta'.format(a*l,(a*l)/2 ))

# Fazendo um algoritmo que lê um preço de um produto e mostre seu seu novo preço, com 5% de desconto
p = float(input('Qual o preço do produto? R$'))

print('O novo preço do produto é: {:2} reais'.format(p*0.95))

#Fazendo um algoritmo que leia o alário de um funciónario e mostre seu novo salário, com 15% de aumento
s = float(input('Qual o seu salário?'))

print('Parabéns! Com seu aumento você passa a receber {:2}'.format(s*1.15))

#Escrevendo um programa que converta uma temperatura digitada em °C e converta para °F
graus = float(input('Informe a temperatura em °C:'))

print('{}°C correspondem a {}°F'.format(graus, ( (graus * 9/5) + 32 )))

#Escrevendo um programa que pergunte a quantidade de KM percorridos por um carro alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e R$0,15 por KM rodado.
dias = int(input('Quantos dias de aluguel?'))
km = float(input('Quantos Kms andou?'))

print('O valor a ser pago é R$ {:.2f}'.format((60 * dias) + (0.15 * km)))

#Criando um programa que lia um número real qualquer pelo teclado e mostre na tela sua porção inteira
import math
n = float(input('Digite um número: '))

print('A parte inteira é {}'.format(math.floor(n)))

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa
import math
x = float(input('Digite o cateto oposto: '))
y = float(input('Digite o cateto adjacente: '))
h = math.hypot(x,y)

print('A hipotenusa é {}'.format(h))

#Fazendo um programa que leia um ângulo qualquer e mostre ma tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite o ângulo: '))

print('O seno é {}, o cosseno é {} e a tangente é {}'.format(math.sin(angulo), math.cos(angulo), math.tan(angulo)))

#Problema: Um professor quer soretar um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o escolhido
import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]
escolhido = random.choices(lista)

print('E o escolhido foi: {}'.format(escolhido))

#Problema:  mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o noem dos quatros alunos e mostre a ordem sorteada
import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]

random.shuffle(lista)

print('A ordem de apresentação será:')
print(lista)

#Criando um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras tem ao todo (sem espaço), quantas letras tem o primeiro nome
nome = input('Qual seu nome completo?').strip()

print('Analisando seu nome...')
print('Seu nome em maísculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count (' ')))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))

#Fazendo um programa que leia um numeeo de 0 a 9999 e mstre na tela cada um dos dígitos separados
numero = int(input('Digite um número com quatro dígitos: '))

print('Analisando seu número... \n {}'.format(numero))
print('A unidade é: {}'.format(numero // 1 % 10))
print('A dezena é: {}'.format(numero // 10 % 10))
print('A centena é: {}'.format(numero // 100 % 10))
print('O milhar é: {}'.format(numero // 1000 % 10))

# Criando um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = str(input('Qual é a cidade?')).upper().strip()

print('Começa com a palvra Santos?')
print(cidade[:5] == 'SANTO')

#Criando um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input('Qual seu nome completo? ')).lower().strip()
print('Seu nome tem Silva? {}'.format('silva' in nome))

#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra 'A', em que posição ela aparece pela primeira vez, em que posição aparece a última vez
frase = str(input('Digite sua frase: ')).lower().strip()

print('A letra A aparece {} vezes'.format(frase.count('a')))
print('Na primeira vez aparece na {}° posição'.format(frase.find('a')+1))
print('Na última vez que aparece esta na {}° posição'.format(frase.rfind('a')+1))

#Fazendo um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

#Problema: Escreva um programa que faça o computador "pensar" em um número inteiro ente 0 e 5 peça paa o usuário tentar descobri qual foi o número escolhido pelo computador. O programa deverá escrever na tela se usuário venceu ou perdeu.
import random 
n = random.choice([0, 1, 2, 3, 4, 5])

print('Já escolhi')
r = input('Digite o número que você acha que eu escolhi: ')
if n == r:
  print('Parabéns! Você acertou!')
else:
  print('Você errou! O número era {}'.format(n))
 
 #Escrevendo um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A mullta vai custar R$ 7,00 por cada KM acima do limite.
 v = float(input('Qual a velocidade? '))
if v > 80:
  print('Você foi multado! O valor da multa é {} reais'.format((v - 80)*7))
else:
  print('Parabéns, cidadão de bem!')
  
  #Criando um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
  n = int(input('Digite seu número: '))

if n % 2 == 0:
  print('É par!')
else:
  print('É ímpar!')
 
#Desenvolvendo um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200 KM e R 0,45 para viagens longas.
km = int(input('Qual a distância? '))
if km  > 200: 
  p = km * 0.45
else:
  p = km * 0.55

print('O preço será {} reais'.format(p))

#Fazendo um programa que leia um ano e mostre se ele é bissexto.
ano = int(input('Digite o ano: '))

if ano % 4 == 0:
  print('O ano de {} é bissexto!'.format(ano))
else:
  print('O ano de {} não é bissexto!'.format(ano))
  
  # Fazendo um programa que leia rês números e mostre qual é o maior e qual é o menor
  n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Mais um: '))
#Verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
  menor = n2
if n3 < n1 and n83 < n2:
  menor = n3

#Verificando maior
maior = n1
if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3

print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))

# Escrevendo um programa que pergunte o salário de um funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s = int(input('Digite o salário: '))
if s > 1250:
  print('O salário é de {} reais'.format(s*1.1))
else:
  print('O salário é de {} reais'.format(s*1.15))
  
 #Desenvolvendo um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triângulo.
 a = int(input('Digite um lado: '))
b = int(input('Digite o outro lado: '))
c = int(input('Digite outro lado: '))

if a < b + c and b < a + c and c < a + b:
  print('Forma um triângulo!')
else:
  print('Não forma um triângulo!')
