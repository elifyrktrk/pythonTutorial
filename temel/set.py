
#Set İle Çalışmak
#Listelere benzerdir
#en önemli özelliği indexsiz ve sırasız elemanlardan oluşmasıdır
#Veri tekrarı yok UNIQUE
#bu veri yapısı performanslı bir data sağlar

#set of integers
my_set = {1, 2, 3}
print(my_set)

#set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

studentsSet = {"Engin","Derin","Salih","Ahmet"}
#Set fonk ile de tanımlanabilir.
studentsSet2 = set("Mehmet","Veli","AYşe")
print(studentsSet)

for student in studentsSet:
    print(student)
    
#true or false
#Derin studentsset içinde var mı?
print("Derin" in studentsSet)

if "Derin" in studentsSet:
    print("Listede var")
else:
    print("Listede yok")
    
#Listede var olan bir eleman değiştirilemez, eleman eklenebilir.

studentsSet.add("Ali")
print(studentsSet)
#genellikle birden fazla işlem yapmak için kullanılır.
studentsSet.update(["Merve","Mert","Selin"])
print(studentsSet)

print(len(studentsSet))
#Silme işlemi
studentsSet.remove("Selin")
print(len(studentsSet))
#geçmişte sildiğim için hata verir.
#studentsSet.remove("Selin")
#print(len(studentsSet))
#discardda böyle bi sorun olmaz.
studentsSet.discard("Selin")
print(len(studentsSet))
#kendi yaptığı sıralamada sırayla siler. 
x = studentsSet.pop()
print(len(studentsSet))
print(studentsSet)
#clear => herşeyi temizler, boş bir sete çevirir.
x = studentsSet.clear()
print(len(studentsSet))
#del=> tüm seti siler
del studentsSet
print(studentsSet)
