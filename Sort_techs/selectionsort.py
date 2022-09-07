#selection sort
'''
Find the minimum element in the array and swap it with the element in the beginning of array
Later from there again find minimum element of the array and swap it and add the element to the 2nd position in the array
and so on upto n elements
Selection sorts the array from the front unlike bubble sort 
It is more efficent than bubble sort
'''

array = [13,46,24,52,20,9]

for index,ele in enumerate(array):
    min_index = index
    #Intially assume the minimum_element is in the current index
    for j in range(index+1,len(array)):
        #for i + 1 checking if the element is less than element in min_index
        if(array[j] < array[min_index]):
            min_index = j
    #swap the elements
    array[index],array[min_index] = array[min_index],array[index]

print(array) 
