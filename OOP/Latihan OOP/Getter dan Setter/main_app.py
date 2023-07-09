class Hero:
  def __init__(self, name,health,armor):
    self.name = name
    self.__health = health
    self.__armor = armor
    #method dibawah ini dipindahkan di bagian property jdi saya komen aja self.infonya
    # self.info = 'name {} : \n\t health {}'.format(self.__name, self.__health) 
  
  #Merubah sebuah methode menjadi seperti variabel
  @property #property ini bisa membuat jadi variabel
  def info(self):
    return 'name {} : \n\t health {}'.format(self.name, self.__health) 
  
  @property
  def armor(self):
    pass

  #Getter untuk armor privat variabel (__armor)
  @armor.getter #getter dari python biar lebih simpel daripada getter OOP
  def armor(self):
    return self.__armor
  
  #Setter untuk armor private variabel (__armor)
  @armor.setter #setter dari python biar lebih simpel daripada setter OOP
  def armor(self,inputArmorBaru):
    self.__armor = inputArmorBaru

  #Deleter untuk menghapus
  @armor.deleter
  def armor(self):
    print('Armor dihapus!')
    self.__armor = None


freya = Hero('freya',100,10)

print('____MERUBAH INFO____')
print(freya.info) #Tidak perlu menggunakan tanda () karena info udah di @property / atau sudah dianggap property / variabel
freya.name = "Bayu"
print(freya.info)

print(30*'=')
print('getter dan setter untuk __armor')
print(freya.armor)
print(freya.__dict__)
freya.armor = 50 #Cara memakai setter di @armor.setter
print(freya.armor)
print(freya.__dict__)

print(30*'=')
print("Deleter untuk menghapus")
del freya.armor #Cara menggunakan deleter / atau cara memakai deleter
print(freya.__dict__)





