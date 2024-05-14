# Định nghĩa lớp Node để biểu diễn mỗi nút trong cây nhị phân
class Node:
    def __init__(self, data):
        self.info = data  # Vùng Info chứa dữ liệu của nút
        self.left = None  # Vùng Left chỉ đến nút con bên trái
        self.right = None  # Vùng Right chỉ đến nút con bên phải
# Phương thức đếm số nút của cây nhị phân
def SoNut(root):
    if root is None:
        return 0  # Nếu cây là None (không tồn tại), trả về số nút là 0
    else:
        # Đệ quy để tính số nút của cây con bên trái, cây con bên phải và cộng thêm 1 (nút gốc)
        return SoNut(root.left) + SoNut(root.right) + 1
# Xây dựng cây nhị phân và tính số nút của cây
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# Test cây nhị phân và in ra số nút của cây
print("Số nút của cây:", SoNut(root))  # Kết quả: 5
