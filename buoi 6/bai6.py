class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

middle_node = find_middle_node(head)
print("Middle node value:", middle_node.value)
