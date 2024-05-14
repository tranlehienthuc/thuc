class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None
def SoNutLa(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return SoNutLa(root.left) + SoNutLa(root.right)
# Test cây nhị phân
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print("Số nút lá của cây:", SoNutLa(root))  # Output: 3
