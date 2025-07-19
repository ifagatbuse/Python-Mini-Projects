sayi = int(input("Bir sayı gir: "))

if sayi > 100:
    print("100'den büyük")
elif sayi == 100:
    print("Tam 100!")
elif sayi > 0:
    print("0 ile 100 arasında")
elif sayi == 0:
    print("Sıfır!")
else:
    print("Negatif sayı")
