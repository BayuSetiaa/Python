#dibawah ini adalah contoh diamond problem
class A:
  def show(self):
    print('Ini adalah show A')

class B(A):
  def show(self):
    print('Ini adalah show B')

class C(A):
  def show(self):
    print('Ini adalah show C')

class D(B,C):
  pass

objek = D()
objek.show()
# help(objek) # ini tools cara untuk melihat urutan dieksekusi yang mana dulu dalam diamond problem