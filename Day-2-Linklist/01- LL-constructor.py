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


status_code_list = LinkedList(404)

print('Head Node Value',status_code_list.head.value)
print('Tail Node Value', status_code_list.tail.value)
print('Length of the LL',status_code_list.length)