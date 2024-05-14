from collections import defaultdict

class DoThi:
    def __init__(self):
        self.dinh = defaultdict(list)  # Danh sách kề của mỗi đỉnh trong đồ thị
        self.cung = 0  # Số cung trong đồ thị (chỉ dùng cho đồ thị có hướng)

    def themCanh(self, u, v):
        # Thêm cạnh từ u đến v
        self.dinh[u].append(v)
        self.cung += 1  # Tăng số cung khi thêm cạnh

    def SoCungVao(self, v):
        # Trả về số cung đi vào đỉnh v
        count = 0
        for u in self.dinh:
            if v in self.dinh[u]:
                count += 1
        return count

# Khởi tạo đồ thị và thêm các cạnh
dt = DoThi()
dt.themCanh(1, 2)
dt.themCanh(2, 3)
dt.themCanh(3, 1)
dt.themCanh(2, 4)
dt.themCanh(4, 1)

# Tính số cung đi vào đỉnh 1 và in kết quả
socung = dt.SoCungVao(1)
print("Số cung đi vào đỉnh 1 là:", socung)
