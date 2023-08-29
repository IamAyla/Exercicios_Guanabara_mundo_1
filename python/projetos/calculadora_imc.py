#Recebendo input das varíaveis
peso = float(input('Digite seu peso: (kg)'))
altura = float(input('Digite sua altura: (m)'))

#Definindo a fórmula
imc = peso/(altura*altura)

#Calculando resultados com condições aninhadas
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
