#Definindo a classe
class Archer:
  arrows = 10
  points = 0
  empty = False
#Definindo os parâmetros para o tiro
  def shoot(self):
    if self.arrows > 0:
      print('Aim... and shoot!')
      self.arrows -= 1
    else:
      self.empty = True
      
#Definindo pontuação para acerto
  def bullseye(self):
    self.points += 3
    
#Definindo a recarga
  def reload(self):
    if self.empty == True:
        self.arrows = 10
        self.empty = False
