# Định nghĩa lớp Node để biểu diễn mỗi nút trong cây nhị phân
class Node:
    def __init__(self, data):
        self.info = data  # Vùng Info chứa dữ liệu của nút
        self.left = None  # Vùng Left chỉ đến nút con bên trái
        self.right = None  # Vùng Right chỉ đến nút con bên phải
# Phương thức kiểm tra xem cây nhị phân có phải là cây BST không
def KiemTraBST(root):
    def isBSTUtil(node, min_value, max_value):
        # Nếu node là None thì đây là cây rỗng, là cây BST
        if node is None:
            return True
        # Kiểm tra giá trị của node nằm trong khoảng giới hạn
        if node.info < min_value or node.info > max_value:
            return False
        # Kiểm tra BST cho cây con bên trái và cây con bên phải
        return (isBSTUtil(node.left, min_value, node.info - 1) and
                isBSTUtil(node.right, node.info + 1, max_value))
    # Gọi hàm trợ giúp để kiểm tra BST từ root với giới hạn là âm vô cùng và dương vô cùng
    return isBSTUtil(root, float("-inf"), float("inf"))
# Xây dựng cây nhị phân
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
# Test và in ra kết quả kiểm tra BST của cây
print("Cây là cây BST:", KiemTraBST(root))  # Kết quả: True
