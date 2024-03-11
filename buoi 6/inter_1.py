class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head):
    if not head or not head.next:
        return head

    seen_values = set()
    current = head
    previous = None

    while current:
        if current.val in seen_values:
            # Loại bỏ node trùng lặp
            previous.next = current.next
        else:
            seen_values.add(current.val)
            previous = current

        current = current.next

    return head

def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
head = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(4, ListNode(5))))))))
print("Input:")
printList(head)

new_head = removeDuplicates(head)

print("\nOutput:")
printList(new_head)
