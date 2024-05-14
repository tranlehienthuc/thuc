from collections import defaultdict

class DoThi:
    def __init__(self):
        self.dinh = defaultdict(list)  # Danh sách kề của mỗi đỉnh trong đồ thị

    def themCanh(self, u, v):
        # Thêm cạnh từ u đến v
        self.dinh[u].append(v)
        # Thêm cạnh từ v đến u (nếu là đồ thị vô hướng)
        self.dinh[v].append(u)

    def ChuaDinh(self, v):
        # Kiểm tra xem đỉnh v có trong danh sách đỉnh của đồ thị không
        return v in self.dinh

# Khởi tạo đồ thị và thêm các cạnh
dt = DoThi()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(2, 3)

# Kiểm tra xem đỉnh 2 có thuộc đồ thị hay không và in kết quả
if dt.ChuaDinh(2):
    print("Đỉnh 2 thuộc đồ thị.")
else:
    print("Đỉnh 2 không thuộc đồ thị.")
