class Node:
    def __init__(self,value):
        self.value= value
        self.next= None

class LinkedList:
    def __init__(self,value):
        new_node= Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
            """
            Prints the values of all nodes in the linked list.
            """
            temp_node = self.head
            while(temp_node is not None):
                print(temp_node.value)
                temp_node = temp_node.next


status_code_list = LinkedList(404)

status_code_list.print_list()