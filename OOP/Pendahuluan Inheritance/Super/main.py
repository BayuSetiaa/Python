class Hero:
  def __init__(self,name,health):
    self.name = name
    self.health = health

  def showInfo(self):
    print('{} dengan Health = {}'.format(self.name, self.health))

class HeroIntellegent(Hero):
  def __init__(self,name):
    # self.name = name   # dua code yang saya comen itu sama aja dgn code yang dibawah ini
    # self.health = 200  # dan disarankan memakai code yang di bawah supaya tdk terjadi pengulangan 
    # Hero.__init__(self,name,100) # atau bisa pakai Super seperti code dibawah ini
    super().__init__(name,100) # kalau udah pakai super gk usah pakai self lagi , dan artinya kita mengambil init yang ada di super
    super().showInfo() # cara memanggil method dengan super dari parent yang dirurunkan di anak

class HeroStrength(Hero):
  def __init__(self,name):
    # untuk code dibawah ini sama saja tinggal kita pilih mau pakai yang mana tpi disarankan pakai yang super karna lebih singkat
    # Hero.__init__(self,name,200)
    super().__init__(name,200)
    super().showInfo()


acel = HeroIntellegent('acel')
adel = HeroStrength('adel')

print(acel.name,' ',acel.health)
print(adel.name,' ',adel.health)

