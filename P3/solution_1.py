def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number<2:
        return number
    
    left, right = 2, number//2
    
    while left <= right:
        pivot = left + (right-left) //2
        
        target = pivot*pivot
        
        if target >number:
            right = pivot - 1
            
        elif target <number:
            left = pivot +1
            
        else:
            return pivot
        
    return right


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")