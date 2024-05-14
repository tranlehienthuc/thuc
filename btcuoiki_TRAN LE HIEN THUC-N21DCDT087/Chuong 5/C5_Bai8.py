class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None


def SoSanh(node1, node2):#Định nghĩa phương thức SoSanh để so sánh hai cây nhị phân.
    # Nếu cả hai cây đều rỗng, chúng giống nhau
    if node1 is None and node2 is None:#Nếu cả hai cây đều rỗng, chúng giống nhau.
        return True

    # Nếu chỉ một trong hai cây rỗng, chúng không giống nhau
    if node1 is None or node2 is None:
        return False

    # So sánh giá trị của nút hiện tại
    if node1.info != node2.info:
        return False

    # Đệ quy so sánh cây con bên trái và cây con bên phải của từng nút
    return SoSanh(node1.left, node2.left) and SoSanh(node1.right, node2.right)


# Sử dụng thử
if __name__ == "__main__":
    # Tạo cây 1
    tree1 = Node(10)
    tree1.left = Node(5)
    tree1.right = Node(15)
    tree1.left.left = Node(2)
    tree1.left.right = Node(7)
    tree1.right.right = Node(20)

    # Tạo cây 2 giống hệt cây 1
    tree2 = Node(10)
    tree2.left = Node(5)
    tree2.right = Node(15)
    tree2.left.left = Node(2)
    tree2.left.right = Node(7)
    tree2.right.right = Node(20)

    # So sánh hai cây
    if SoSanh(tree1, tree2):
        print("Hai cay giong nhau hoan toan")
    else:
        print("Hai cay khong giong nhau hoan toan")
