class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head

def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Example 1
head1 = ListNode(1, ListNode(1, ListNode(2)))
print("Input:")
printList(head1)
new_head1 = deleteDuplicates(head1)
print("\nOutput:")
printList(new_head1)

# Example 2
head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print("\nInput:")
printList(head2)
new_head2 = deleteDuplicates(head2)
print("\nOutput:")
printList(new_head2)
