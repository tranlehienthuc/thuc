# Định nghĩa lớp Node để biểu diễn mỗi nút trong cây nhị phân
class Node:
    def __init__(self, data):
        self.info = data  # Vùng Info chứa dữ liệu của nút
        self.left = None  # Vùng Left chỉ đến nút con bên trái
        self.right = None  # Vùng Right chỉ đến nút con bên phải
# Phương thức đếm số nút trung gian của cây nhị phân
def SoNutTrungGian(root):
    if root is None or (root.left is None and root.right is None):
        return 0  # Trường hợp cây rỗng hoặc cây chỉ có một nút (nút lá)
    elif root.left is not None and root.right is not None:
        # Nếu nút hiện tại có cả hai cây con, đây là nút trung gian
        return 1 + SoNutTrungGian(root.left) + SoNutTrungGian(root.right)
    else:
        # Nếu nút hiện tại chỉ có một trong hai cây con (hoặc không có cây con), đệ quy tính số nút trung gian của cây con bên trái hoặc bên phải
        return SoNutTrungGian(root.left) + SoNutTrungGian(root.right)
# Xây dựng cây nhị phân
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
# Test và in ra số nút trung gian của cây
print("Số nút trung gian của cây:", SoNutTrungGian(root))  # Kết quả: 2
