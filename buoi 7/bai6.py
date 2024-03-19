class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def isEmpty(self):
        return self.linked_list.head is None

    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

# Printing the stack by traversing the linked list
current = customStack.linked_list.head
while current:
    print(current.value)
    current = current.next
