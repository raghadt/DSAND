"""
Balanced Parentheses Exercise
In this exercise you are going to apply what you learned about stacks with a real world problem. We will be using stacks to make sure the parentheses are balanced in mathematical expressions such as: ((32+8)∗(5/2))/(2+6). In real life you can see this extend to many things such as text editor plugins and interactive development environments for all sorts of bracket completion checks.

Take a string as an input and return True if it's parentheses are balanced or False if it is not.

Try to code up a solution and pass the test cases.

"""
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """

    stack = Stack()
    
    
    for i in equation:
        if i=='(':
            stack.push(i)
        elif i==')':
            if stack.pop() == None:
                return False
    
    print(stack.size())
    return stack.size()==0


# =======================================================================
