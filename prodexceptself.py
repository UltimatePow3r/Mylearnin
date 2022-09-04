list1=[]
n = int(input("Enter the number of elements in array\n"))

print("Enter the numbers:\n")
for i in range(n):
    ele = int(input())
    list1.append(ele)
prod = 1
for i in list1:
    prod = prod * i

for index, element in enumerate(list1) :
    list1[index] = int(prod / element)

print(list1)