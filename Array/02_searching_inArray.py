arr = [1, 2, 3, 4, 5, 13, 21, 34, 55, 89]
target = 89


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Element {target} found at index {i}")
            return i
    print(f"Element {target} not found in the array")
    return -1       

def binary_search(arr, target):
    left, right = 0 , len(arr) - 1 
    while left <= right:
        mid = left + (right - left) // 2
        if (target == arr[mid]):
            return mid
        elif (target > arr[mid]):
            left = mid + 1
        else:
            right = mid - 1
    return -1
    

def binary_search_recursive(arr, left, right, target):
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    if(target > arr[mid]):
        return binary_search_recursive(arr, mid + 1, right, target)
    elif (target < arr[mid]) :
        return binary_search_recursive(arr, left, mid - 1, target)
    else:
        return mid 


answer_linear = linear_search(arr, target)
answer_binary = binary_search(arr, target)
answer_recursive = binary_search_recursive(arr , 0 , len(arr) - 1, target)



if( answer_linear != -1 or answer_binary != -1):
    print(f"Found the target value at index " , answer_binary)
    print (f"Found using the recursive approach also " , answer_recursive)
else:
    print (f"Target not found")