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

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

# Example usage:
linked_list = LinkedList(2)
linked_list.add_node(3)
linked_list.add_node(4)

print("Original Linked List:")
current_node = linked_list.head
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")

linked_list.insert_at_beginning(1)

print("\nLinked List after Insertion at Beginning:")
current_node = linked_list.head
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")
