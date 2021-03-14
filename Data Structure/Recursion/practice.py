def is_palindrome(input_):
    """
    Return True if input is palindrome, False otherwise.
    
    Args:
       input(str): input to be checked if it is palindrome
    """
    
    # TODO: Write your recursive palindrome checker here
    if input_ == "":
        return True
    
    first_char = input_[0]
    last_char = input_[-1]
    
    if first_char != last_char:
        return False
    return is_palindrome(input_[1:-1])
        