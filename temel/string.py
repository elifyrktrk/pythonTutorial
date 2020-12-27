
#substring
mesaj = "Merhaba Dünya"
print(mesaj[2:5])
yeniMesaj = mesaj[12:13]
print(yeniMesaj)

#Len
print(len(mesaj))
yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

#Lower Upper
print(mesaj.lower())
print(mesaj.upper())

#replace
print(mesaj.replace("ü","u"))
print(mesaj)

print(mesaj.replace("a","e"))

#Split Strip
#splitin defaultu boşluktur.
bilgi = "Elif; Yürektürk; 21; Denizli"
print(bilgi.split())
print("yaşı: " + bilgi.split(";")[2])

#input
ad = input("adınız?")
sayi1 = input("Sayi1 = ?")
sayi2 = input("Sayi2 = ?")
print(int(sayi1) + int(sayi2))