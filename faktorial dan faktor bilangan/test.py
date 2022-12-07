

import os
from time import sleep

clear = lambda: os.system('cls')

def cek_input():
  counter = 3
  cek = False

  while not cek:
    clear()
    counter -= 1
    n = input('Masukkan nilai faktorial: ')

    try:
        val = int(n)
        cek = True
        return val

    except ValueError:

        if counter == 0:
          return 'Anda sudah melakukan 3x percobaan harap coba beberapa saat lagi'

        print('Masukkan input angka')
        sleep(3)

def faktorial(n):

  if n > 2:
    return n * faktorial(n - 1)
  elif n == 1 or n == 0 :
    return 1
  else:
    return 'tak terdefinisi'

int_nilai = cek_input()
nilai = faktorial(int_nilai)
print(f'Hasil dari {int_nilai}! = {nilai}')

def cek_input():
  counter = 3
  cek = False

  while not cek:
    clear()
    counter -= 1
    n = input('Masukkan bilangan: ')
    
    try:
        val = int(n)
        cek = True
        return val

    except ValueError:

        if counter == 0:
          return 'Anda sudah melakukan 3x percobaan harap coba beberapa saat lagi'

        print('Masukkan input angka')
        sleep(3)

def faktor(n):
  faktor = []

  for i in range(1, n + 1):
      if n % i == 0:
          faktor.append(i)
  return faktor[0:]

int_nilai = cek_input()
nilai = faktor(int_nilai)
print(f'Faktor dari {int_nilai} = {nilai}')