
#toplu yorum satırına alma kısayolu ctrl+1


sehirler = ["Ankara","Istanbul","Izmır"]

#print(sehirler[0])
#print(sehirler[1])
#print(sehirler[2])


#bu şekilde hücrelere ayırıyoruz ve ayrı ayrı çalıştırabiliyoruz.
#%%
for sehir in sehirler:
    if sehir =="Istanbul":
        #break #döngüyü kırar!
        continue #sadece şart sağlandığı andaki durumu iptal eder.
        
    print(sehir+" için kod = "+sehir[0:3])
    print("***")#if in içinde olmadığından dolayı Ankara için de yıldız basar.
#%%   
for x in range(2,100,2):
    print(x)