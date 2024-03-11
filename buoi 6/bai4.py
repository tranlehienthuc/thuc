class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_node(self, index):
        if index < 0:
            print("Invalid index. Index should be non-negative.")
            return None

        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
            deleted_node.next = None
            return deleted_node

        current = self.head
        prev = None
        count = 0

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if not current:
            print("Index out of range. Cannot delete node.")
            return None

        deleted_node = current
        prev.next = current.next
        deleted_node.next = None
        return deleted_node

# Example usage:
linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

index_to_delete = 1
deleted_node = linked_list.delete_node(index_to_delete)

if deleted_node:
    print(f"Node with data {deleted_node.data} at index {index_to_delete} deleted.")
else:
    print("Node deletion unsuccessful.")
