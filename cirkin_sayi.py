import numpy as np

def asalMi(sayi):
    if sayi == 1:
        return False
    if sayi == 2:
        return True
    if sayi % 2 == 0:
        return False
    for i in range(3, int(sayi**0.5) + 1, 2):
        if sayi % i == 0:
            return False
    return True

def asal_sayilari_bul(n):
    asallar = []
    for sayi in range(2, n + 1):
        if asalMi(sayi):
            asallar.append(sayi)
    return asallar

yuz_e_kadar_asallar = asal_sayilari_bul(100)
print("100'e kadar olan asal sayılar:", yuz_e_kadar_asallar)

# 2, 3, 5 hariç diğer asal sayılar
asallar = np.delete(yuz_e_kadar_asallar, [0, 1, 2])
print("2, 3, 5 hariç diğer asal sayılar:", asallar)

num = int(input("num : "))

# Çirkin sayı kontrolü
if any(num % asal == 0  for asal in asallar):
    print(f"{num} çirkin bir sayıdır.")
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
    print(f"{num} çirkin bir sayı değildir.")
