
# !class isimleri büyük harfle başlanır.

#%%Basics
class Matematik:
    def __init__ (self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    #self sınıf içerisindeki metodlara, parametrelere ulaşmak için kullanılabilir.
    def bol(self):
        return self.sayi1 / self.sayi2
#self parametresi ile ilgili sınıfa ait metod ve parametreleri kullanacağınızı işaret edersiniz.
matematik = Matematik(2,78)
mat2 = Matematik(3,76)
print("Toplam = " + str(mat2.topla()))

#%% Property

class Person:
    #init = constructor
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Elif","Yürektürk",21)
print(person1.firstName)
    #classın yanına (Person) yazarak inheritence örneği oluşturdum. 
class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        

class Customer(Person):
    def __init__(self,cresitCardNumber):
        self.cresitCardNumber = cresitCardNumber
        
    
    