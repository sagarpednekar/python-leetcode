class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Prints the values of all nodes in the linked list.
        """
        temp_node = self.head
        while (temp_node is not None):
            print(temp_node.value)
            temp_node = temp_node.next

    def append(self, value):
        """
        Scenario 1- List is empty
        Scneario 2- List has more than 1 element
        O(1) - operation 
        """
        new_node = Node(value)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


status_code_list = LinkedList(400)

# status_code_list.print_list()

status_code_list.append(404)

status_code_list.print_list()


## Object represetation of LL
""" 
LinkedList {
    head: Node {
        value: 400,
        next: Node {
            value: 404,
            next: None
        }
    },
    tail: Node {
        value: 404,
        next: None
    },
    length: 2
}
"""
# if we miss updating tail node on line 34 the our linklist will look like
"""
LinkedList {
    head: Node {
        value: 400,
        next: Node {
            value: 404,
            next: None
        }
    },
    tail: Node {
        value: 400,
        next: Node {
            value: 404,
            next: None
        }
    },
    length: 2
}
"""