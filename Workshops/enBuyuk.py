
sayi = int(input('1. sayi :'))
sayi1 = int(input('2. sayi :'))
sayi2 = int(input('3. sayi :'))

enBuyuk = sayi

if (sayi1 > sayi) and (sayi1 > sayi2):
    enBuyuk = sayi1
elif (sayi2 > sayi1) and (sayi2 > sayi):
    enBuyuk = sayi2
else:
    enBuyuk = sayi
    
print(enBuyuk)