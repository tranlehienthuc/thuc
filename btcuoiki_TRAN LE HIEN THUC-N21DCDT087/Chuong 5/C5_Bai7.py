class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None
def Chep(root):#Định nghĩa phương thức Chep để sao chép một cây nhị phân.
    # Nếu cây rỗng, trả về None vì không cần sao chép
    if root is None:#Kiểm tra xem cây cần sao chép có rỗng không. Nếu rỗng, trả về None vì không cần sao chép.
        return None
    # Tạo một nút mới với giá trị từ nút gốc của cây cần sao chép
    new_node = Node(root.info)# Tạo một nút mới với giá trị từ nút gốc của cây cần sao chép.
    # Đệ quy sao chép cây con bên trái và cây con bên phải của nút hiện tại
    new_node.left = Chep(root.left)#Đệ quy sao chép cây con bên trái của nút hiện tại.
    new_node.right = Chep(root.right)#Đệ quy sao chép cây con bên phải của nút hiện tại.
    # Trả về nút mới đã sao chép và được kết nối đầy đủ với các cây con
    return new_node#Trả về nút mới đã sao chép và được kết nối đầy đủ với các cây con.
# Sử dụng thử
if __name__ == "__main__":
    # Tạo cây ban đầu
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.right = Node(20)
    # Sao chép cây ban đầu
    copied_tree = Chep(root)
    # In cây sao chép để kiểm tra
    def print_tree(node):
        if node:
            print_tree(node.left)
            print(node.info, end=" ")
            print_tree(node.right)
    print("Cay goc:")
    print_tree(root)
    print("\nCay da sao chep:")
    print_tree(copied_tree)
