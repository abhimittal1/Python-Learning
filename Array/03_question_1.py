"""
array = [10, 22, -3, 4, 0, 3, 1, 34, 55, 89, inf, inf , inf, inf, inf, inf, inf, inf, inf, inf]
question = "Find the first occurrence of the infinite value in the array"

"""
from cmath import inf

array = [10, 22, -3, 4, 0, 3, 1, 34, 55, 89, inf, inf , inf, inf, inf, inf, inf, inf, inf, inf]

"""
1. We can apply the linear search algorithm to find the first occurrence of the infinite value in the array. The linear search algorithm works by iterating through each element of the array and checking if it matches the target value (in this case, infinity).
        But the time complexity of linear search is O(n), where n is the number of elements in the array. This means that in the worst case, we may have to check every element in the array before finding the target value.
        
2 . We can also apply the binary search algorithm to find the first occurrence of the infinite value in the array. The binary search algorithm works by repeatedly dividing the search interval in half. If the value of the target is less than the value in the middle of the interval, we narrow the interval to the lower half. Otherwise, we narrow it to the upper half. We continue this process until we find the target value or the interval is empty.
        But the time complexity of binary search is O(log n), where n is the number of elements in the array. This means that in the worst case, we may have to check log n elements before finding the target value. However, binary search requires that the array be sorted, which is not the case here since the infinite values are at the end of the array.
 
3. We can also apply the jump search algorithm to find the first occurrence of the infinite value in the array. The jump search algorithm works by dividing the array into blocks of a fixed size and jumping ahead by that block size until we find a block that contains the target value. Once we find a block that contains the target value, we perform a linear search within that block to find the first occurrence of the target value.
        But the time complexity of jump search is O(√n), where n is the number of elements in the array. This means that in the worst case, we may have to check √n elements before finding the target value. However, jump search also requires that the array be sorted, which is not the case here since the infinite values are at the end of the array.
        
4. We can also apply the exponential search algorithm to find the first occurrence of the infinite value in the array. The exponential search algorithm works by first finding a range where the target value may be located, and then performing a binary search within that range. We start by checking the first element of the array, and if it is not the target value, we double the index until we find an index that is greater than or equal to the target value. Once we have found a range, we perform a binary search within that range to find the first occurrence of the target value.       
        But the time complexity of exponential search is O(log n), where n is the number of elements in the array. This means that in the worst case, we may have to check log n elements before finding the target value. However, exponential search also requires that the array be sorted, which is not the case here since the infinite values are at the end of the array.         
        
"""
def find_first_occurrence_of_infinity(array):
    for index, value in enumerate(array):
        if value == inf:
            return index
    return -1  # Return -1 if infinity is not found

def find_first_occurrence_of_inf_by_binary_search(array):
    left, right = 0, len(array) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == inf:
            result = mid
            right = mid - 1  # Continue searching in the left half
        else:
            left = mid + 1  # Search in the right half

    return result

def find_first_occurrence_of_inf_by_jump_search(array):
    n = len(array)
    step = int(n**0.5)  # Calculate the block size
    prev = 0

    while array[min(step, n) - 1] < inf:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1  # Infinity not found

    # Perform linear search in the identified block
    for index in range(prev, min(step, n)):
        if array[index] == inf:
            return index

    return -1  # Return -1 if infinity is not found

def find_first_occurrence_of_inf_by_exponential_search(array):
    if array[0] == inf:
        return 0

    index = 1
    while index < len(array) and array[index] < inf:
        index *= 2

    left = index // 2
    right = min(index, len(array) - 1)

    # Perform binary search in the identified range
    result = -1
    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == inf:
            result = mid
            right = mid - 1  # Continue searching in the left half
        else:
            left = mid + 1  # Search in the right half

    return result

def print_array(array):
    print("Array:", array)
    
    

def main():
    print_array(array)
    index = find_first_occurrence_of_infinity(array)
    index_binary = find_first_occurrence_of_inf_by_binary_search(array)
    index_jump = find_first_occurrence_of_inf_by_jump_search(array)
    index_exponential = find_first_occurrence_of_inf_by_exponential_search(array)
    if index != -1:
        print(f"The first occurrence of infinity is at index: {index}")
        print(f"Binary search result: {index_binary}")
        print(f"Jump search result: {index_jump}")
        print(f"Exponential search result: {index_exponential}")
    else:
        print("Infinity is not found in the array.")

if __name__ == "__main__":
    main()
