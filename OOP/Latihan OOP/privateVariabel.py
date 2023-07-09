#Episode 7 mengenal privat variabel
class Hero:
  #class variabel 
  jumlah = 0

  #variabel private di class / cara membuat variabel private di class
  __privateJumlah = 0
  def __init__(self, name,health):
    self.name = name
    self.health = health

    #variabel instance private / cara membuat varibel privat di methode
    self.__private = "private"

    #variabel instance protected / cara membuat varibel protected di methode
    self._protected = "protected"



freya = Hero("freya",100)

print(freya.__dict__)
print(Hero.__dict__)


