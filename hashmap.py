#take a string as input and count the number of all the things in that
from collections import Counter

str1 = input("Enter a string")

#print(Counter(str1)) 

#hashmap way
hashmap={}

for i in str1:
    hashmap[i] = 1 + hashmap.get(i,0)

print(hashmap)