
# brute force approach
def brute_search_2d(matrix, target):
    for i in range(len(matrix)):
        for j in  range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
    
    return False        
    
def binary_serach_2d(matrix, target):
    """
    We can convert the 2D into 1D then apply binary 
    left = 0 and right = (m*n-1) --> total number of elements from here we can get the mid
    for conversion to 2D again  ---> m = mid // m  ,, n = mid % n
    
    divide for rows and modul for columns
    
    """
    left = 0
    right = ( len(matrix) * len(matrix[0]) ) - 1
    
    while (left <= right):
        mid = left + ( right - left ) // 2 
        row  = mid // len(matrix[0])
        col = mid % len(matrix[0])
        
        if matrix[row][col] == target: return True
        
        elif matrix[row][col] < target:
            left = mid + 1
        
        else: 
            right = mid - 1
                
    return False        



matrix = [[1,3,5,7] , [10,11,14,15], [132,142,421,3634]]
target = 142
result = brute_search_2d(matrix, target)
result_2 = binary_serach_2d(matrix, target)
print(result , "This is from the Brute Force with time complex -- (m * n)")
print(f"This is from the binary Search with Time Complex -- (log mn) : " , result_2)