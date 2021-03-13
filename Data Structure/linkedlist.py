
# Exercise 1 - Implementing a simple linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
print(head.value) #2



# Exercise 2 - Traversing the list

def print_values(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


# Creating a linked list using iteration

def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """

    head = None

    for i in input_list:
        if head is None:
            head = Node(i)
        else:
            curr_node = head 
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = Node(i)

    return head


#------------------------------------------------------
# --------- Types of Linked Lists ---------------------
#------------------------------------------------------

# 1. Single Linkedlist



class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next: #if node.next is empty
            node = node.next #add the a 'node.next'
        
        node.next = Node(value) # node.next add the value
        return




# 2. Doubly Linked Lists
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        
        
        return
    
# 3. Circular Linked Lists





#------------------------------------------------------
# --------- Linked List Practice ---------------------
#------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Task 1. Write definition of prepend() function and test its functionality

def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    node = Node(value)
    node.next = self.head
    self.head = node
    
    return


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend


# Task 2. Write definition of append() function and test its functionality

def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here    
    if self.head is None:
        self.head = Node(value)
        return

    node = self.head
    while node.next:
        node = node.next

    node.next = Node(value)

LinkedList.append = append


# Task 3. Write definition of search() function and test its functionality

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    if self.head is None:
        return None

    node = self.head
    while node:
        if node.value == value:
            return node
        node = node.next

    raise ValueError("Value not found in the list.")


# Task 4. Write definition of remove() function and test its functionality

def remove(self, value):
    """ Delete the first node with the desired data. """
    if self.head is None:
        return

    if self.head.value == value:
        self.head = self.head.next
        return

    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            return
        node = node.next

    raise ValueError("Value not found in the list.")



# Task 5. Write definition of pop() function and test its functionality

def pop(self):
    """ Return the first node's value and remove it from the list. """
    if self.head is None:
        return None

    node = self.head
    self.head = self.head.next

    return node.value