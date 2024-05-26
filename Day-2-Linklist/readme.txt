Note:

Here are the time complexities for common operations 
on a singly linked list:

Insertion:

prepend(value): At the start: O(1)
append(value): At the end: O(n) (if we don't have a tail pointer), O(1) (if we have a tail pointer)
insertAfter(node, value): In the middle: O(n)
Deletion:

deleteFirst(value): From the start: O(1)
deleteLast(): From the end: O(n)
deleteNode(node): From the middle: O(n)
Searching: search(value): O(n)

Accessing an element by index: getNode(index): O(n)

Comparision with Array 

Insertion:

At the start: list.insert(0, value): O(n)
At the end: list.append(value): O(1) (amortized time)
In the middle: list.insert(index, value): O(n)
Deletion:

From the start: list.pop(0): O(n)
From the end: list.pop(): O(1)
From the middle: list.pop(index): O(n)
Searching: value in list: O(n)

Accessing an element by index: list[index]: O(1)

