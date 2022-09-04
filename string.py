from collections import Counter
string12 = "abcd this is testing string"

print(Counter(string12)) 
list12 = [1,1,1,1,2,2,2,3,4,5,6,2,3]
print(Counter(list12)) #counter can be run on list also 
print("\n")

print(tuple(string12)) 

print(string12[1:6]) 

a =10.2345
b = str(round(a,2))#round float to 2 points
print(type(b))
print(b) 

'''
string1=input("Enter a string with all types of character")
print(string1.lower())
'''

string1="testing123"
print(string1.isalpha()) 
tesstring = "split,this,string"

print(len(tesstring.split(','))) 