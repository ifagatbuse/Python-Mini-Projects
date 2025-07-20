sayilar = []

for i in range(5):
    girdi = int(input("enter a number"))  # ← Bu satır girintili olmalı
    sayilar.append(girdi)

for s in sayilar:
    if s % 2 == 0:
        print("even num", s)
