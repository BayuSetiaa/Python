def menu():
  print('---Menu---')
  print('1.tambah')
  print('2.kurang')
  print('3.kali')
  print('4.bagi')

def tambah (a, b):
  return a+b

def kurang (a, b):
  return a-b

def kali (a, b):
  return a*b

def bagi (a, b):
  return a/b

while True:
  menu()
  
  pilih = int(input('Masukan Pilihan Menu = '))
  
  match pilih:
    case 1 : print(f'Hasil tambah adalah = {tambah(2,3)}')
    case 2 : print(f'Hasil kurang adalah = {kurang(6,3)}')
    case 3 : print(f'Hasil kali adalah = {kali(5,2)}')
    case 4 : print(f'Hasil bagi adalah = {bagi(10,2)}')
  
  isDone = str(input('Apakah ingin lanjut(y/n)'))

  if isDone == "n":
    break

print('akhir dari program')