# Định nghĩa lớp Node đại diện cho một nút trong cây nhị phân
class Node:
    def __init__(self, info=None, left=None, right=None):
        self.info = info  # Thông tin của nút
        self.left = left  # Nút con trái
        self.right = right  # Nút con phải

# Hàm kiểm tra hai cây có giống nhau không
def is_identical(node1, node2):
    # Nếu cả hai cây đều là None, chúng giống nhau
    if node1 is None and node2 is None:
        return True
    # Nếu một trong hai cây là None, chúng không giống nhau
    if node1 is None or node2 is None:
        return False
    # Kiểm tra thông tin của nút và kiểm tra các cây con của chúng
    return (node1.info == node2.info and
            is_identical(node1.left, node2.left) and
            is_identical(node1.right, node2.right))

# Hàm kiểm tra cây 2 có là cây con của cây 1 không
def is_subtree(cay1, cay2):
    # Nếu cây 2 là None, nó là cây con của mọi cây
    if cay2 is None:
        return True
    # Nếu cây 1 là None và cây 2 không phải, cây 2 không thể là cây con
    if cay1 is None:
        return False
    # Nếu cây 2 giống với cây 1, cây 2 là cây con của cây 1
    if is_identical(cay1, cay2):
        return True
    # Kiểm tra các cây con bên trái và bên phải của cây 1
    return is_subtree(cay1.left, cay2) or is_subtree(cay1.right, cay2)
# Sử dụng:
# Tạo cây 1
cay1 = Node(1)
cay1.left = Node(2)
cay1.right = Node(3)
cay1.left.left = Node(4)
cay1.left.right = Node(5)

# Tạo cây 2
cay2 = Node(2)
cay2.left = Node(4)
cay2.right = Node(5)

# Kiểm tra xem cây 2 có là cây con của cây 1 không
if is_subtree(cay1, cay2):
    print("cay2 la cay con cua cay1")
else:
    print("cay2 khong phai la cay con cua cay1")
