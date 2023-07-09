class Hero:
  def __init__(self,name,health,attackPower,armorNumber):
    self.name = name
    self.health = health
    self.attackPower = attackPower
    self.ararmorNumber =armorNumber

  def serang(self,lawan):
    print(self.name, 'Menyerang', lawan.name)
    lawan.diserang(self,self.attackPower)

  def diserang(self,lawan, attackPower_lawan):
    print(self.name, 'Diserang', lawan.name)
    attack_diterima = attackPower_lawan/self.ararmorNumber
    print('serangan terasa = ',attack_diterima)
    self.health -= attack_diterima
    print(f'Jumlah Health {self.name} = {self.health}')

freya = Hero('freya',100,10,5)
angelchan = Hero('angelchan',100,20,10 )

print()
freya.serang(angelchan)
print()
angelchan.serang(freya)

