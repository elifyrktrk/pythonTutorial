

#Dictionary
# Aynen set gibi sırasız veri tutar.
#Günlük hayattaki sözlükler gibi kullanabiliriz.

sozluk = {
        "book" : "kitap",
        "table" : "masa"
        }
#constructor için böyle bir tanımlama da yapılabilir.
sozluk2 = dict(kitap = "book", masa = "table")

sozluk["book"] = "kitap 1"
sozluk["pencil"] = "kalem"
#silme islemi del ile
del(sozluk["book"])
print(len(sozluk))

