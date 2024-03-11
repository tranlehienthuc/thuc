class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    if not head:
        return None

    seen_values = set()
    current = head
    previous = None

    while current:
        if current.value in seen_values:
            # Loại bỏ nút nếu giá trị đã xuất hiện trước đó
            previous.next = current.next
        else:
            seen_values.add(current.value)
            previous = current

        current = current.next

    return head

# Example usage:
# Tạo một danh sách liên kết đơn: 1 -> 2 -> 4 -> 3 -> 4 -> 2
head = ListNode(1, ListNode(2, ListNode(4, ListNode(3, ListNode(4, ListNode(2))))))

print("Original Linked List:")
current = head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

# Loại bỏ các phần tử trùng lặp
head = remove_duplicates(head)

print("\nResult Linked List:")
current = head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
