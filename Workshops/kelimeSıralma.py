
cumle = "Bugün hava cok güzel"

#istenilen çıktı:
#
#bugün
#cok
#güzel
#hava

kelimeler = cumle.split()
kelimeler.sort()
print(kelimeler)

for kelime in kelimeler:
    print(kelime)