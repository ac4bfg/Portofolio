import os
from time import sleep

clear = lambda: os.system('cls')

def faktorial(n):
  if n > 2:
    return n * faktorial(n - 1)
  elif n == 1 or n == 0 :
    return 1
  elif n < 0:
    return 'tak terdefinisi'

  return 2

def faktor(n):
  faktor = []

  for i in range(1, n + 1):
      if n % i == 0:
          faktor.append(i)
  return faktor[0:]

os.system('cls')
str_jenis_input = '''Program pencarian faktor bilangan & faktorial

Pilih jenis pencarian :
1. Faktor bilangan
2. Faktorial

Masukkan input = '''

jenis_input = input(str_jenis_input)

if jenis_input == '1':
    os.system('cls')
    for x in range(3):
      bilangan = input('Masukkan bilangan = ')
      try:
          bilangan = int(bilangan)
          break
      except ValueError:
          print('input bilangan harus berupa angka')
          sleep(3)
          os.system('cls')
    
    if x >= 2:
      print('teralu banyak percobaan input harap ulangi beberapa saat lagi')
      exit()
    else:
      nilai = faktor(bilangan)
      print(f'Faktor dari {bilangan} = {nilai}')
    
elif jenis_input == '2':
    os.system('cls')

    for x in range(3):
      bilangan = input('Masukkan nilai faktorial = ')

      try:
        bilangan = int(bilangan)
        break

      except ValueError:
        print('input bilangan harus berupa angka')
        sleep(3)
        os.system('cls')
    
    if x >= 2:
      print('teralu banyak percobaan input harap ulangi beberapa saat lagi')
      exit()
    else:
      nilai = faktorial(bilangan)
      print(f'Hasil dari {bilangan}! = {nilai}')
else:
    print('input tidak tersedia')