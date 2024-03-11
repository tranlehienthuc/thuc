class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)

print("Danh sách liên kết ban đầu:")
llist.printList()

llist.reverse()
print("\nDanh sách liên kết sau khi đảo ngược:")
llist.printList()
