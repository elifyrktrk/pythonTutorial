
sayi = int(input("Bir sayı giriniz: "))
asalMi = True
for x in range(2,sayi):
    if (sayi%x) == 0:
        asalMi = False
        break
    
if asalMi: #== True   defaultu True dur.
    print("ASAL")
else:
    print("ASAL DEGIL!")