class Team:
  def setTeam (self, team):
    self.team = team
  
  def showTeam (self):
    print(self.team)

class Tipe_hero:
  def setTipe(self, tipe):
    self.tipe = tipe
  
  def showTipe (self):
    print(self.tipe)

class Hero(Team, Tipe_hero):
  def __init__(self,name,health):
    self.name = name
    self.health = health

freya = Hero('freya',100)
freya.setTeam('MERAH')
freya.setTipe('Tipe Hero Cantik')

freya.showTeam()
freya.showTipe()
