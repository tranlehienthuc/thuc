# Định nghĩa lớp Node để biểu diễn mỗi nút trong cây nhị phân
class Node:
    def __init__(self, data):
        self.info = data  # Vùng Info chứa dữ liệu của nút
        self.left = None  # Vùng Left chỉ đến nút con bên trái
        self.right = None  # Vùng Right chỉ đến nút con bên phải
# Phương thức tính chiều cao của cây nhị phân
def ChieuCao(root):
    if root is None:
        return -1  # Chiều cao của cây rỗng là -1
    else:
        # Tính chiều cao của cây con bên trái và cây con bên phải
        left_height = ChieuCao(root.left)
        right_height = ChieuCao(root.right)
        # Chiều cao của cây hiện tại bằng chiều cao lớn nhất của hai cây con cộng thêm 1 (nút gốc)
        return max(left_height, right_height) + 1
# Xây dựng cây nhị phân
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# Test và in ra chiều cao của cây
print("Chiều cao của cây:", ChieuCao(root))  # Kết quả: 2
