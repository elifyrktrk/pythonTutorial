
fak=1

sayi = int(input("Sayı giriniz: "))

if sayi==0:
    print("Faktöriyel: 1")
elif sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz")
else:
    for x in range(1,sayi+1):
        fak = fak*x
    print("Faktöriyel: ",fak)
    