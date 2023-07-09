# Membuat class abstract
# abc = abstract base class

from abc import ABC,abstractmethod

class Button(ABC):
  
  @abstractmethod
  def click(self):
    pass

class PushButton(Button):

  def click(self):
    print('Push Button Click')

class RadioButton(Button):

  def click(self):
    print('Radio Button Click')

tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()
