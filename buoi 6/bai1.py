class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        initial_node = Node(value)
        self.head = initial_node
        self.tail = initial_node
        self.length = 1

    def add_node(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

# Example usage:
linked_list = LinkedList(1)
linked_list.add_node(2)
linked_list.add_node(3)

print("Linked List:")
current_node = linked_list.head
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")
