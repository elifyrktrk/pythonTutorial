
def topla(sayi1,sayi2):
    return sayi1+sayi2

def cikar(sayi1,sayi2):
    return sayi1-sayi2

def carp(sayi1,sayi2):
    return sayi1*sayi2

def bol(sayi1,sayi2):
    return sayi1/sayi2

print("Operation Menu?")
print("1: Topla")
print("2: Çıkar")
print("3: Çarp")
print("4: Böl")

sec = int(input("Menüden bir işlem seçiniz"))


#Ben bu şekilde yaptım bir de fonk tanımlayarak yapalım. 
#if sec == 1:
#    sonuc = sayi1 + sayi2
#elif sec == 2:
#    sonuc = sayi1 - sayi2
#elif sec == 3:
#    sonuc = sayi1 * sayi2
#elif sec == 4:
#    sonuc = sayi1/sayi2
#else:
#    print("Gecersiz Secenek! Lütfen menüden bir sayı giriniz")
#
#print(sonuc)

if (sec != 1 or sec != 2 or sec != 3 or sec != 4):
    print("Gecersiz secenek")
else:
    sayi1 = int(input("sayi1:"))
    sayi2 = int(input("sayi2:"))
    
if sec == 1:
    print(topla(sayi1,sayi2))
elif sec == 2:
    print(cikar(sayi1,sayi2))
elif sec == 3:
    print(carp(sayi1,sayi2))
elif sec == 4:
    print(bol(sayi1,sayi2))
else:
    print("Lütfen menüden bir sayı giriniz")


