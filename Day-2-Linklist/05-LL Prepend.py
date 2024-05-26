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

    def pop(self):
        """
        Removes and returns the value of the last node in the linked list.
        Returns:
            The value of the last node in the linked list, or None if the list is empty.
        o(n) - operation
        """
        if self.length == 0:
            return None
        else:
            pre = self.head
            temp = self.head
            while (temp.next):
                pre = temp
                temp = temp.next
            if (temp.next is None):
                self.tail = pre
                self.tail.next = None  # breaks link
            self.length -= 1
            if (self.length == 0):
                self.head = None
                self.tail = None
            return temp.value

    def prepend(self, value):
        """
        Scenario 1: LL is empty
        Scenario 2: LL has more than 1 elements
        o(1) operation
        """
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        Scenario 1 - LL is empty
        Scenario 2- LL has only one element
        Scenario 3- LL has more than 1 elements
        """
        if (self.length == 0):
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if (self.length == 0):
                self.tail = None
            return temp.value


status_code_list = LinkedList(400)

status_code_list.append(404)

status_code_list.append(500)

status_code_list.pop_first()

status_code_list.print_list()


status_code_list.prepend(200)

# status_code_list.pop_first()

# # status_code_list.pop_first()

# status_code_list.pop_first()


# status_code_list.print_list()



