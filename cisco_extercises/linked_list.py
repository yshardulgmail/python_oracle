class Node:
  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:  
    def __init__(self):  
        self.head = None  
  
    def add_node(self, data):  
        newNode = Node(data)  
        if self.head != None:  
            current = self.head  
            while (current.next):  
                current = current.next  
            current.next = newNode  
        else:  
            return None  
  
    def reverse_Llist(self):  
        if self.head == Node:  
            return None  
  
        previous = None  
        current = self.head  
        after = current.next   
    
        while current:  
            # Reverse the link  
            current.next = previous  
            # Moving previous element to one ahead  
            previous = current  
            # Moving current one element ahead  
            current = after  
            # Moving one element ahead  
            if after:  
                after = after.next  
    
        self.head = previous  
  
    def print_list(self):  
        if self.head is not None:  
            current = self.head  
            while current:  
                print(current.data)  
                current = current.next  
  
n = LinkedList()  
n.head = Node(1)  
n1 = Node(2)  
n.head.next = n1  
n2 = Node(3)  
n1.next = n2  
n3 = Node(4)  
n2.next = n3  
  
n.print_list()  
print("\nReversed List:")
n.reverse_Llist()
n.print_list()