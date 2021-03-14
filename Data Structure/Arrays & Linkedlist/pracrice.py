#----- Duplicate-Number ------

"""
You have been given an array of length = n. The array contains integers from 0 to n - 2. Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array
Example:
arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)

"""

def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    
    current_sum  = 0
    for i in arr:
        current_sum+= i
    expected_sum = 0
    for i in range(len(arr)-1):
        expected_sum += i
    
    print(current_sum)
    print(expected_sum)
    
    print(current_sum-expected_sum)
    
    return current_sum-expected_sum
duplicate_number([0,1,1,2])



# -------- Max-Sum-Subarray -----------

"""
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.
Example 1:
arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.
Example 2:
arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.
"""

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    
    curr_sum = arr[0]
    max_sum = arr[0]


    for i in range(1, len(arr)):
        curr_sum = max(curr_sum+arr[i], arr[i])
        max_sum = max(curr_sum, max_sum)
        
    return max_sum




# ---------- Pascal's-Triangle --------------
def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n == 0:
        return [1]
    
    triangle = []
    
    for num_row in range(n+1):
        row = [None for _ in range(num_row+1)] #create empty triangle
        row[0] = row[-1] = 1 # fille edges with 1
        
        for j in range(1, len(row)-1): #work on the inside
            row[j] = triangle[num_row-1][j-1] + triangle[num_row-1][j]
        triangle.append(row)
    return row
            

