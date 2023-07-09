class Hero:
  #privat variabel class
  __jumlah = 0 

  def __init__(self, name,health,attackPower,armor):
    self.__name = name
    self.__healthStandar = health
    self.__attackPowerStandar = attackPower
    self.__armorStandar = armor
    self.__level = 1
    self.__exp = 0

    self.__healthMax = self.__healthStandar * self.__level
    self.__attackPower = self.__attackPowerStandar * self.__level
    self.__armor = self.__armorStandar * self.__level

    self.__health = self.__healthMax
    
    Hero.__jumlah += 1

  @property
  def info(self):
    return '{} Level {} : \n\tHealth = {}/{} \n\t Attack = {} \n\t Armor = {}'.format(self.__name,self.__level,self.__health,self.__healthMax,self.__attackPower,self.__armor)
  
  @property
  def gainExp(self): #gain exp artinya untuk mendapatkan experience
    pass

  @gainExp.setter
  def gainExp(self,addExp):
    self.__exp += addExp
    if self.__exp >= 100:
      print(self.__name,'Level Up!')
      self.__level += 1
      self.__exp -= 100

      self.__healthMax = self.__healthStandar * self.__level
      self.__attackPower = self.__attackPowerStandar * self.__level
      self.__armor = self.__armorStandar * self.__level

  def attack(self,musuh):
    self.gainExp = 50




freya = Hero('freya',100,5,10)
acel = Hero('acel',100,5,10)
print(freya.info)

freya.attack(acel)
freya.attack(acel)
freya.attack(acel)
print(freya.info)
