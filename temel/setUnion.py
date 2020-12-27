
#set union ile çalışmak
#   . . .  . . .
# . 1     .      .
#.   2  . 3 . 4   .
# .      .     5 .
#  .    .  .    .
#   . .     . .
#setUnion = (1,2,3,4,5) her elemanı bir kez yazar

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

#set intersection sadece ortak elemanlar
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

#set difference / fark
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

#symmetric difference => sadece A ve sadece B 
print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))