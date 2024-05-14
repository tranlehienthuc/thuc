class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, info):
        new_node = Node(info)
        new_node.next = self.head
        self.head = new_node
        
    def dao_nguoc(self):
        if self.head is None or self.head.next is None:
            return  

        stack = []
        current = self.head

        while current:
            stack.append(current)
            current = current.next

        self.head = stack.pop()
        current = self.head

    
        while stack:
            next_node = stack.pop()
            current.next = next_node
            current = next_node
        current.next = None

    def print_list(self):
        current = self.head
        while current:
            print(current.info, end=" ")
            current = current.next
        print()

linked_list = LinkedList()
linked_list.add(5)
linked_list.add(4)
linked_list.add(3)
linked_list.add(2)
linked_list.add(1)

print("Danh sách ban đầu:")
linked_list.print_list()
linked_list.dao_nguoc()
print("Danh sách sau khi đảo ngược:")
linked_list.print_list()
