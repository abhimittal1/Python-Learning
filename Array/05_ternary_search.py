"""
This is like the binary search works on the sorted array, 
    here we divid array in Three equal halfs
    
"""

def ternarySearch(left , right, target, matrix):

    while left <= right:
        mid_1 = left + (right - left) // 3
        mid_2 = right - (right - left) // 3
        
        # For the first Search Space
        if target == matrix[mid_1]:
            return mid_1
        elif target == matrix[mid_2]:
            return mid_2 
        
        # for the 3rd search space
        elif target < matrix[mid_1]:
            return ternarySearch(left , mid_1 -1, target, matrix)
        
        elif target > matrix[mid_2]:
            return ternarySearch(mid_2 + 1 , right, target, matrix)

        # For the 2nd search space
        else:
            return ternarySearch(mid_1 + 1, mid_2 -1 , target , matrix)
   
    return -1


matrix = [1,2,3,4,5,6,7,8,9]
left = 0
right = len(matrix) - 1
target = 91
result = ternarySearch(left , right, target, matrix)
print(f"This is the result from the ternary Search : " , result)