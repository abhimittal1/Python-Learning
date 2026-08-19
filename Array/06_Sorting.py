"""
We have the 2 types of Sorting ALgo : 

        Comparison Based                           Non Comparison Based
        
    1. Selection Sort                          1. Count Sort 
    2. Bubble Sort                             2. Radix Sort 
    3. insertion Sort                          3. Bucket Sort 
    4. Quick Sort
    5. Merge Sort
    6. Heap Sort    
        
Always know the approach and Scenarios --> Time and space Complexity
"""

"""
Stable vs Unstable Sorting Algo :
    Stable Sorting Algo : Relative order should be maintained after applying the sorting algo
        Example : 
    
    Unstable Sorting Algo : Relative order is not maintained after applying the sorting algo
        Example : Quick Sort , Heap Sort and Selection Sort are Unstable Sorting Algo
"""

"""
Inplace and Outplace Sorting Algo :
    Inplace Sorting Algo : Sorting is done in the same array and no extra space is used
        Example : Bubble Sort , Insertion Sort , Quick Sort and Heap Sort are Inplace Sorting Algo
        
    Outplace Sorting Algo : Sorting is done in a different array and extra space is used
        Example : Merge Sort and Count Sort are Outplace Sorting Algo
"""

def bubble_sort_arr(arr):
    for i in range(len(arr)):
        for j in range( len(arr) - i - 1 ):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
                
    return arr            
                
                
def selection_sort_arr(arr):
    starting_index = 0
    while starting_index < len(arr):
        min_index = starting_index  
        for i in range(starting_index + 1, len(arr)):
            if arr[min_index] >= arr[i]:
                min_index = i
        arr[starting_index] , arr[min_index] = arr[min_index] , arr[starting_index]
        starting_index += 1
        
    return arr    
            
def insertion_sort_arr(arr):   
    
     
    
    
array = [24,2,5,2,5,4,2,9,45,2,6,25,4,5,25,2,5,26,54,655,72,846,6,568,352,2625654,9,3568,0,72,6,256,35,39,658,68,6,7,7,568,67,467,234]

bubble_sort = bubble_sort_arr(array)
selection_sort = selection_sort_arr(array)
insertion_sort = insertion_sort_arr(array)


print(f"This is the result from the Bubble Sort : " , bubble_sort)
print(f"This is the result from the Selection Sort : " , selection_sort)
print(f"This is the result from the Insertion Sort : " , insertion_sort)



print(f"hello world")