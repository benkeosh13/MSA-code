"""
function to perform quick sort of array
input: list
output: sorted list
"""

def quicksort(arr):
    #create a stack to simular recursive calls
    stack = []
    #place partitions on the stack
    stack.append((0,len(arr)-1))
    #inside while loop. Loop runs until stack of partitions is empty
    while stack:
        #get next partition to proccess
        low, high = stack.pop()
        #partition the array. find the pivot index for that partition. call the partition fuction
        pivot_index = partition(arr, low, high)
        #if there are items on the left of the pivot, put them on the stack
        if pivot_index - 1 > low:
            stack.append((low, pivot_index -1))
        #if there are items on the right of pivot, put then on the stack
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))

"""
function to find partition index in a list
Inputs: list(arr), (int)low, int(high)
output: (int)partition index
"""
def partition(arr, low, high):
    #Choose the rightmost item as the pivot
    pivot = arr[high]
    #create a variable for the border
    i = low-1
    #loop through the partition to place all items <= the pivot to the left. An >= the pivot to the right
    for j in range(low,high):
        #if the current item is less than the pivot, swap it with the element at the border
        if arr[j] <=pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    #place the pivot in correct position
    #swap the pivot with the item at the border
    arr[i+1],arr[high] = arr[high], arr[i+1]
    
    return i + 1
    

def main():
    #create a list
    arr = [40,80,10,90,30,50,70]   
    quicksort(arr)
    print(arr)

main()