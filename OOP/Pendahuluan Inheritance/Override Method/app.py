class Hero:
  def __init__(self,name,health):
    self.name = name
    self.health = health
  
  def showInfo(self): 
    print('Show info di class Hero') 
    print('{} dengan Health: {}'.format(self.name, self.health))


class HeroIntelligent(Hero):
  def __init__(self,name):
    super().__init__(name,100) #ini untuk mengambil , override di bawah untuk menimpa, override == menimpa
  
  #override
  def showInfo(self): # ini yang dimaksud membuat method override atau pengertiannya yaitu menimpa method/fungsi yang ada di super class
    print('Show info di sub class Hero Inteligent') 
    print('{} \n\t Tipe = Intelligent \n\t Health = {}'.format(self.name, self.health))

class HeroStrength(Hero):
  def __init__(self,name):
    super().__init__(name,200)


freya = HeroIntelligent('freya')
acel = HeroStrength('acel')

print()
freya.showInfo()
print()
acel.showInfo()
