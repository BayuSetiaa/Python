class Hero:
  #private class variabel
  __jumlah = 0

  def __init__(self, name):
    self.__name = name
    Hero.__jumlah += 1
  
  #Methode ini berlaku hanya untuk objek karena ada self
  def getJumlah(self):
    return Hero.__jumlah
  
  #Methode berlaku untuk class karena tidak ada self
  def getJumlah1():
    return Hero.__jumlah
  
  #static method (decorator) bisa berlaku untuk dua-duanya 
  @staticmethod # ini adalah cara membuat static methode nya supaya nempel di class dan bisa dipakai diobjek
  def getJumlah2():
    return Hero.__jumlah
  
  #sama kaya static method tpi ada argumenya jadi lebih keren dan lumayan rekomended
  @classmethod
  def getJumlah3(cls): #Nama argumenya bebas bisa apa aja gk harus cls
    return cls.__jumlah



freya = Hero('freya')
print(Hero.getJumlah2())

bayu = Hero('bayu')
print(bayu.getJumlah2())

acel = Hero('acel')
print(Hero.getJumlah3())

chirsty = Hero('chirsty')
print(chirsty.getJumlah3())