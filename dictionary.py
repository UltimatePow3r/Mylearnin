from ast import comprehension
from collections import defaultdict
from itertools import product
dicti={}

dicti[10] = "abc"

print(dicti) 
print(dicti.get(20,"default"))  

dicti[20] = "def" 


print(dicti)
for i in dicti:
    print(i) # printing the keys

#map two lists to each other in python

list1=[5,10,15]
list2=[1,2,3,4]
dict1={}

#dict1=dict(zip(list2,list1))
dict1={list1[i]:list2[i] for i in range(len(list1))}
#We can also do this using comprehension
print(dict1)

str="0000123500"

number = str.count('0')
print(number)

defdict = defaultdict(list)
defdict[tuple(list1)].append("test")

defdict["hellotester"].append("hello the")
defdict["hellotester"].append("hello the 2")
defdict["int value"].append(2)

#print(defdict["hellotester"][0])

for key,values in defdict.items():
    for i in values:
        if(i == 2):
            print(key)

#print(defdict)

'''
dict2={1:'a',2:'b',3:'c'} 

for i,j in dict2.items():
    print(f"\n{i}:{j}") 

'''

dicttes={1:'a'}

if 1 in dicttes: 
    print("\nkey is default")


dictmax={1:1,2:2,3:3}

print(dictmax[max(dictmax.keys())]) 

print(dictmax[max(dictmax.values())]) 

floavar = 10.23755
print(type(floavar))
storevar = round(floavar,2)
print(storevar)



