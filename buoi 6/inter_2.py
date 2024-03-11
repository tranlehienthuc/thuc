class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def nth_to_last(self, n):
        if n <= 0:
            print("Invalid value of n.")
            return None

        slow_ptr = fast_ptr = self.head

        # Move fast_ptr n nodes ahead
        for _ in range(n):
            if fast_ptr is None:
                print("The linked list does not have enough elements.")
                return None
            fast_ptr = fast_ptr.next

        # Move both pointers until fast_ptr reaches the end
        while fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        return slow_ptr.data

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

n = 2  # Replace with the desired value of n
result = linked_list.nth_to_last(n)

if result is not None:
    print(f"The {n}th to last element is: {result}")
