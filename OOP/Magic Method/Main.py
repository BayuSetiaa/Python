class Mangga:
  #tanda magic method adalah ada __nama method__ , ada tanda __...__
  # contoh magic method seperti di bawah ini
  def __init__(self,nama,jumlah):
    self.nama = nama
    self.jumlah = jumlah
  
  def __repr__(self): #ini sama aja tpi biasanya dipakai untuk debug
    return 'Debug -> Mangga = {} dengan Jumlah = {}'.format(self.nama,self.jumlah)

  def __str__(self): #ini yang direkomendasi untuk dipakai 
    return 'Mangga = {} dengan Jumlah = {}'.format(self.nama,self.jumlah)
  
  #magic method yang berguna untuk aritmatika
  def __add__(self,objek) :
    return self.jumlah + objek.jumlah
  
  #override magic method __dict__
  @property
  def __dict__(self):
    return 'Objek Ini Mempunyai Nama dan Jumlah '


  #magic method untuk selanjutnya masih banyak kita tinggal search di google aja ada banyak.
  # atau kalau ingin cari magic method yang lain searching didokumentasi python yg resmi

belanja1 = Mangga('Arum manis',10)
belanja2 = Mangga('Kueni',5)

# print(repr(belanja1)) #ini cara pakai kalau pakai repr 

print(belanja1)
print(belanja2)

print(belanja1 + belanja2) #cara memakai magic method __add__

print(belanja1.__dict__) # __dict__ juga termasuk magic method 