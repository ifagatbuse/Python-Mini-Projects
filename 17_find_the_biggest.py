
sayilar = [] 

for i in range(5):
    girdi = int(input("Bir sayı girin: ")) 
    sayilar.append(girdi) 


biggest = sayilar[0]


for s in sayilar:
    if s > biggest:
        biggest = s 

print("En büyük sayı:", biggest)

