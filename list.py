#lists

from platform import freedesktop_os_release

listest = [ i for i in range(1,10)]
print(listest) 

#frequency
freq = [[] for i in range(1,10)]
freq[0]=["a","list","inside","list"]
print(freq)

list2 = [i for i in range(10,-1,-1)]#decromaner for reverse in order 
print(list2)

list2=[1,2,3,4,5]

print(list2.pop())# Deletes last element from the list
print(list2.index(2)) #returns the index of current value in the list
print(list2.index(max(list2))) #returns the index of max value from the list

list2.sort(reverse=True)#sorts the list in descending order 
print(list2)

list3 = listest + list2

print(list3)   

numbers = ['a','b','c']
a = numbers[:]#
print(a)

newstr = "".join(numbers)
print(newstr)

