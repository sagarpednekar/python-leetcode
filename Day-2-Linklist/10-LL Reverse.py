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

    def get(self, index):
        """
        Case1 : index > length
        Case2 : Anywhere in the list
        """

        if (index >= self.length or index < 0):
            return None
        else:
            temp = self.head
            count = 0
            while (count < index):
                temp = temp.next
                count += 1
        return temp

    def set_value(self, index, value):
        if (index < 0 or index > self.length):
            return None
        else:
            temp = self.get(index)
            if (temp):
                temp.value = value
                return True

    def insert(self, index, value):
        if (index < 0 or index > self.length):
            return False
        if (index == 0):
            return self.prepend(value)
        if (index == self.length):
            return self.append(value)
        temp = self.get(index-1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if (index < 0 or index > self.length):
            return None
        if (index == 0):
            return self.pop_first()
        if (index == self.length):
            return self.pop()
        temp = self.get(index-1)
        element = self.get(index)
        temp.next = element.next
        element.next = None
        self.length -= 1
        return element.value

    def reverse(self):
        """
        Case 1 : LL is empty
        Case 2 : LL has one element
        Case 2 : Has more than 3 elements
        """
        if (self.length == 1):
            return self
        else:
            # reverse head and tail
            temp = self.head
            self.head = self.tail
            self.tail = temp
            after = temp.next
            before = None
            for _ in range(self.length):
                after = temp.next
                temp.next = before
                before = temp
                temp = after
            return True

status_code_list = LinkedList(400)


status_code_list.insert(1, 200)

status_code_list.insert(0, 202)

status_code_list.insert(3, 201)

status_code_list.insert(2, 404)

print('Before reverse')
status_code_list.print_list()




status_code_list.reverse()

print('After reverse\n')

status_code_list.print_list()
