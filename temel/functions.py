
sehir = "Ankara"

print(sehir.upper())
print(sehir.endswith("e"))

def selamVer(isim = "dostum"):#default parametreli fonk.
    #eğer birden fazla parametre verilecekse default param. en sonda olmalı!
    print("Merhaba " + isim)
    
selamVer("Elif")
selamVer()

def ucgenAlanHes(a,b):
    return a*b/2

alan = ucgenAlanHes(2,3)

print(alan)

#%%
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla2(3,6))

print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2

print(x(4,5))