class Hero:
  def __init__(self, name,health,attackPower):
    self.__name = name #ini private variabel karena menggunakan __(nama variabel kita yg mau diprivate) 
    self.__health = health #ini private variabel karena menggunakan __(nama variabel kita yg mau diprivate)
    self.__attackPower = attackPower #ini private variabel karena menggunakan __(nama variabel kita yg mau diprivate)

  #getter
  def getName(self):
    return self.__name
  
  def getHealth(self):
    return self.__health
  
  #setter
  def diserang(self,damageSerang):
    self.__health -= damageSerang
  
  def setAttPower(self,powerBaru):
    self.__attackPower = powerBaru
    


#Awal dari game
freya = Hero("freya",100,5)
print(freya.__dict__)

#Game berjalan 
print('Nama Hero')
print(freya.getName())

print(30*'=')

print('Sebelum Diserang')
print(freya.getHealth())

print(30*'=')

print('Sesudah Diserang')
freya.diserang(5)
print(freya.getHealth())

