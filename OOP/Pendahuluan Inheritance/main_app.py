class Hero:
  def __init__(self,name,health):
    self.name = name
    self.health = health
  
class HeroIntellegent(Hero):
  pass

class HeroStrength(Hero):
  pass



freya = Hero('freya',100)
acel = HeroIntellegent('acel',50)
adel = HeroStrength('adel',200)

print(freya.name)
print(acel.name)
print(adel.name)
