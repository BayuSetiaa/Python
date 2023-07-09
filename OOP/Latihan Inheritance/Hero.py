class Hero:
  def __init__(self,name):
    self.healthPool = [0,100,200,300,400,500]
    self.attackPowerPool = [0,10,20,30,40,50,]
    self.armorPool = [0,1,2,3,4,5]

    self.__name = name
    self.__exp = 0
    self.__level = 0
  
  def show_info(self): # kalau penulisan method harus dikasil tanda _ : ex : show_info bukan showInfo
    print('{} \n\t Level = {} \n\t Health = {} \n\t Attack Power = {} \n\t Armor = {}'.format(self.__name,self.__level,self.__health ,self.__attackPower,self.__armor))

  @property
  def healthPool(self):
    pass

  @property
  def attackPowerPool(self):
    pass

  @property
  def armorPool(self):
    pass

  @property
  def levelUp(self):
    pass

  @property
  def gainExp(self):
    pass

  @healthPool.setter
  def healthPool(self,input):
    self.__healthPool = input

  @attackPowerPool.setter
  def attackPowerPool(self,input):
    self.__attackPowerPool = input

  @armorPool.setter
  def armorPool(self,input):
    self.__armorPool = input

  @gainExp.setter
  def gainExp(self,input):
    self.__exp += input
    if self.__exp >= 100:
      self.levelUp = self.__exp // 100
      self.__exp %= 100
  
  @levelUp.setter
  def levelUp(self,input):
    self.__level += input
    self.__health = self.__healthPool[self.__level]
    self.__attackPower = self.__attackPowerPool[self.__level]
    self.__armor = self.__armorPool[self.__level]

class HeroIntelligent(Hero): #penulisanya jangan pakai _ kalau class ,ex : Hero_intelligent , _ tanda itu dipakai kalau membuat method atau fungsi aja
  def __init__(self, name):
    super().__init__(name)
    self.healthPool = [0,50,100,150,200,250]
    self.attackPowerPool = [0,20,40,60,80,100]
    self.armorPool = [0,0.5,1,1.5,2,2.5]
    self.levelUp = 1

class HeroStrength(Hero):
  def __init__(self, name):
    super().__init__(name)
    self.healthPool = [0,200,300,400,500,600]
    self.attackPowerPool = [0,20,40,60,80,100]
    self.armorPool = [0,2,4,6,8,10] 
    self.levelUp = 1

