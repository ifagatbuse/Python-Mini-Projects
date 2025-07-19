print("Dört İşlem Hesap Makinesi")
print("İşlem türünü seçin: +, -, *, /")

islem = input("İşlem seç: ")
sayi1 = float(input("1. sayıyı gir: "))
sayi2 = float(input("2. sayıyı gir: "))

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Hata: Sıfıra bölünemez!")
else:
    print("Geçersiz işlem seçimi.")
