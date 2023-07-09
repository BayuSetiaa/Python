while True:
  angka = int(input('Masukan Angka Pembagi = '))
  try:
    hasil = 10/angka
    print(f'Hasilnya Adalah = {hasil}')
    pilih = str(input('Apakah ingin lanjut (y/n)'))
    if pilih == 'n':
      break
  except:
    print('Pembagi tidak boleh nol\nSilahkan Coba Masukan Angka Lagi')

print('Akhir dari program')