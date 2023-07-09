# Pendahuluan Class
# class Hero:
#   pass

# hero1 = Hero()
# hero2 = Hero()

# hero1.name = "bayu"
# hero1.health = 200
# hero2.name = "freya"
# hero2.health = 200

# print(hero1)
# print(f'Nama Hero {hero1.name}')
# print(f'Nama Hero {hero2.name}')
# print(f'Health Hero {hero1.health}')
# print(f'Health Hero {hero2.health}')
# print(hero1.__dict__)

# Lanjutan episode 2
# class Hero: # def __init__ di eksekusi pertama
#   def __init__(self,inputName,inputHealth,inputPower): # (hero1.name) sama saja dengan (self.name) jadi (self) itu sama dengan (hero1)
#     self.name = inputName
#     self.healht = inputHealth
#     self.power = inputPower

# hero1 = Hero("Freya",100,200)

# print(hero1.__dict__)
# print(f'Nama Hero {hero1.name}')
# print(f'Health Hero {hero1.healht}')
# print(f'Power hero {hero1.power}')

# Lanjutan Episode 3
# class Hero:
#   jumlah = 0 # class variabel
#   def __init__(self,inputName,inputHealth,inputPower): # (hero1.name) sama saja dengan (self.name) jadi (self) itu sama dengan (hero1)
#     self.name = inputName
#     self.healht = inputHealth
#     self.power = inputPower
#     Hero.jumlah += 1
#     print('Membuat Hero Dengan Nama' , inputName)

# hero1 = Hero("Freya",100,200)
# print(Hero.jumlah)
# hero2 = Hero('Bayu',50,20)
# print(Hero.jumlah)

# Lanjutan Episode 4
class Hero:
  jumlah = 0 
  def __init__(self,inputName,inputHealth,inputPower):
    self.name = inputName
    self.healht = inputHealth
    self.power = inputPower
    Hero.jumlah += 1
  
  def sayName(self): # Methode tanpa return dan tanpa argument
    print(f'Namaku Adalah {self.name}')

  def healthUp(self,up): # Methode dengan argumen
    self.healht += up

  def getHealth(self): # Methode dengan return
    return self.healht


hero1 = Hero("Freya",100,200)
hero2 = Hero('Bayu',50,20)

hero1.sayName() # Cara Memanggil methode tanpa return dan argumen

hero1.healthUp(10)
print(hero1.healht) # Cara memanggil methode dengan argumen

print(hero1.getHealth()) # Cara memanggil methode dengan return







