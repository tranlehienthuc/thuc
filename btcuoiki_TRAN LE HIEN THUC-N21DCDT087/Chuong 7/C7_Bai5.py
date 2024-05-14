from collections import defaultdict

class DoThi:
    def __init__(self):
        self.dinh = defaultdict(list)  # Danh sách kề của mỗi đỉnh trong đồ thị

    def themCanh(self, u, v):
        # Thêm cạnh từ u đến v
        self.dinh[u].append(v)
        # Thêm cạnh từ v đến u (vô hướng)
        self.dinh[v].append(u)

    def BacDinh(self, v):
        # Trả về số lượng đỉnh kề của đỉnh v
        return len(self.dinh[v])

# Khởi tạo đồ thị và thêm các cạnh
dt = DoThi()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(2, 3)

# Tính bậc của đỉnh 2 và in kết quả
bac = dt.BacDinh(2)
print("Bậc của đỉnh 2 là:", bac)
