class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class DSLK:
    def __init__(self):
        self.head = None

    def them_vao_dau(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def in_nguoc_de_qui(self, node):
        if node is None:
            return
        self.in_nguoc_de_qui(node.next)
        print(node.info, end =" ")

    def in_nguoc_khong_de_qui(self):
        if self.head is None:
            return
        stack = []
        current = self.head
        while current is not None:
            stack.append(current)
            current = current.next
        while stack:
            print(stack.pop().info, end =" ")

danh_sach = DSLK()
danh_sach.them_vao_dau(1)
danh_sach.them_vao_dau(2)
danh_sach.them_vao_dau(3)
danh_sach.them_vao_dau(4)
danh_sach.them_vao_dau(5)

print("Danh sách liên kết ngược sử dụng đệ qui:", end =" ")
danh_sach.in_nguoc_de_qui(danh_sach.head)
print()

print("Danh sách liên kết ngược không sử dụng đệ qui:", end =" ")
danh_sach.in_nguoc_khong_de_qui()


