#Atribuindo a classe jogador
class Player:
  def __init__(self,name):
        self.name = name

#Atribuindo a classe computador, considerando o jogador
class Computer(Player):
  def __init__(self):
    super().__init__('NPC')
    
#Definindo a resposta do computador com o input do nome
  def respond(self,player):
    print('Hello,', player.name, 'I am', self.name)
    
#Atribuindo a classe usuário, considerando o jogad or
class User(Player):
  def __init__(self, name, level):
    super().__init__(name)
#Definindo a saudação
  def greet(self):
    print('Hi! What is your name?')

computer = Computer()
user = User('Ayla', 1)
user.greet()
computer.respond(user)
