
#yorum satırı kısayol => ctrl+1

#ogrenci1 = "elif"
#ogrenci2 = "emine"
#ogrenci3 = "zeynep"
#
#print(ogrenci1)
#print(ogrenci2)
#print(ogrenci3)

ogrenciler = ["elif","emine","zeynep"]


print(ogrenciler[1])
#append  => yeni ogrenci ekleme
ogrenciler.append("Ahmet")
ogrenciler[3] = "Veli"
print(ogrenciler[3])
#remove => öğrenci kaldırma
ogrenciler.remove("elif")
print(ogrenciler)

#list constructor => liste oluşturucu
sehirler = list(("Ankara","İstanbul","Ankara"))
print(sehirler)
print(len(sehirler))

#diğer fonksiyonlar
#print(sehirler.clear())
print("Ankara sayisi = " + str(sehirler.count("Ankara")))
print("Ankara indeksi = " + str(sehirler.index("Ankara")))
#pop => çıkarma
sehirler.pop(1)
#insert => ekleme
sehirler.insert(0,"İstanbul")
sehirler.reverse()

sehirler3 = sehirler.copy()

sehirler2 = sehirler
sehirler2[0]="İzmir"

print(sehirler3)
print(sehirler2)
print(sehirler)

#extend => birleştirir ekler
sehirler.extend(sehirler3)
print(sehirler)

#sort => sıralama
sehirler.sort()
#reverse => tersine çevirir
sehirler.reverse()
print(sehirler )

#***TUPLE***
#listelere benzerdir
#tek farkı listelerde elemanları değiştirebilirken,tupleda değiştirilemez.
#bu veri yapısı performanslı bir data sağlar




