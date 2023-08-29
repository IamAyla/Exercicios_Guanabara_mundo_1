#Atribuindo a classe do refrigerante
class Soda_Machine:
  paid = False
  balance = 0

#Definindo a ejeção do refri
  def eject_soda(self):
    if paid == False:
      print('Please insert money')
    else:
      print('Enjoy the soda!')

#Definindo pagamento
  def pay(self, amount):
    self.balance += amount

#Definindo a seleção do refrigerante
  def select_soda(self):
    if balance >= 1:
      self.paid = True
      self.balance -= True 
    else:
      self.paid = False
