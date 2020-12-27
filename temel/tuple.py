

#***TUPLE***
#listelere benzerdir
#tek farkı listelerde elemanları değiştirebilirken,tupleda değiştirilemez.
#bu veri yapısı performanslı bir data sağlar

tupleListe = (2,4,6,"Ankara",(2,3,4),[])
liste = [2,4,6,"Ankara",[3,4,5],()]

liste[0]=6
#tupleListe[0]=6

tupleDeger = ("Elif") 
print(type(tupleDeger))

#-2 => sondan ikinci eleman
print(tupleListe[1:2])
print(liste[1:2])

print(tupleListe[-2])
print(liste[-2])

print(type(tupleListe))
print(type(liste))
print(tupleListe)
print(liste)
print(len(tupleListe))
print(len(liste))  