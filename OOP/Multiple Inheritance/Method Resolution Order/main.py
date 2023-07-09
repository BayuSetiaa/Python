class A:
  def show(self):
    print('Ini adalah show A')

class B:
  def show(self):
    print('Ini adalah show B')

class C(A,B): #yang dimaksud method resolution order adalah urutan eksekusi ,disitu kan C(A,B) berati yang ditampilin shownya show A, kalau di ubah jadi C(B,A) maka show yg akan ditampilin adalah show B terlebih dahulu
  pass

objek = C()
objek.show()