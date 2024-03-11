class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy_head = ListNode()
    current = dummy_head

    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # Nối danh sách còn lại (nếu có)
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy_head.next

# Example usage:
# Tạo hai danh sách liên kết đã sắp xếp: list1 = [1, 2, 4], list2 = [1, 3, 4]
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

print("List 1:")
current = list1
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

print("\nList 2:")
current = list2
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

# Hợp nhất hai danh sách liên kết
merged_list = merge_sorted_lists(list1, list2)

print("\nMerged List:")
current = merged_list
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
