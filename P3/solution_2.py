def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the number
    Returns:
       int: Index or -1
    """

    # ----------- fix this
    start = 0
    end = len(input_list) - 1 

    while start <= end:
        pivot = (start + end)//2 


        if input_list[pivot] == number:
            return pivot

        if input_list[pivot] > input_list[end]: 
            if  input_list[start] <= number and number < input_list[pivot]:
                end = pivot - 1
            else: #
                start = pivot + 1

        else: 
            if  input_list[pivot] < number and number <= input_list[end]:
                start = pivot + 1
            else: 
                end = pivot - 1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])