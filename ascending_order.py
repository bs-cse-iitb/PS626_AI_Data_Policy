import random
#insertion sort
def ascending_order(list1):
    size = len(list1)
    for i in range(1, size): 
        key = list1[i]
        j = i-1
        while j >= 0 and key < list1[j] :
                list1[j+1] = list1[j]
                j = j - 1
        list1[j+1] = key        
    return list1

random.seed(0)
no_of_element=50
numbers = [random.randint(1,no_of_element) for i in range(no_of_element)]
print("Unsorted number:",numbers)

sorted_numbers = ascending_order(numbers)
print("Sorted numbers in ascending order:", sorted_numbers)