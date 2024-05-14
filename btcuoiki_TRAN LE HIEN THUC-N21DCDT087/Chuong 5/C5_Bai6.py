class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None
        self.height = 1  # chiều cao của nút
#Hàm height(node) trả về chiều cao của nút node. Nếu node là None, nghĩa là nút không tồn tại, ta trả về 0.
def height(node):
    if node is None:
        return 0
    return node.height
#Hàm get_balance(node) tính toán và trả về giá trị cân bằng của nút node,là hiệu của chiều cao của nút con trái và phải.
def get_balance(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)
#Hàm update_height(node) cập nhật chiều cao của nút node dựa trên chiều cao của nút con trái và phải.
def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))
#Hàm rotate_right(y) thực hiện quay phải (right rotation) cho nút y, và trả về nút mới sau khi quay.
def rotate_right(y):
    x = y.left
    T2 = x.right

    # Thực hiện quay
    x.right = y
    y.left = T2

    # Cập nhật chiều cao
    update_height(y)
    update_height(x)

    return x
#Hàm rotate_left(x) thực hiện quay trái (left rotation) cho nút x, và trả về nút mới sau khi quay.
def rotate_left(x):
    y = x.right
    T2 = y.left

    # Thực hiện quay
    y.left = x
    x.right = T2

    # Cập nhật chiều cao
    update_height(x)
    update_height(y)
    return y
#Hàm KiemTraAVL(root) kiểm tra xem cây có gốc root có phải là cây AVL không bằng cách kiểm tra cân bằng tại nút gốc và các nút con, đệ quy qua toàn bộ cây.
def KiemTraAVL(root):
    if root is None:
        return True

    balance = get_balance(root)

    # Kiểm tra cân bằng
    if abs(balance) > 1:
        return False
    # Kiểm tra cân bằng cho các nút con
    return KiemTraAVL(root.left) and KiemTraAVL(root.right)

# Sử dụng thử
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.right = Node(20)

    if KiemTraAVL(root):
        print("Cay nay la cay AVL")
    else:
        print("Cay nay khong la cay AVL")
