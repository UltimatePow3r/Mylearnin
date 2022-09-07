'''
Swap the adjacent two elements until the greatest element appears at last
Sorting is done from the back unlike selection sort it is done from the front
'''

array = [13,46,24,52,20,9]

n = len(array)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
swapped = False
for i in range(n-1):
    #it is not required to run last time because they are already in place
    for j in range(0, n-i-1):
        if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
         
    if not swapped:
        break

print(array)
  