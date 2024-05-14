from collections import defaultdict

class DoThi:
    def __init__(self):
        self.dinh = defaultdict(list)  # Danh sách kề của mỗi đỉnh trong đồ thị
        self.cung = 0  # Số cung trong đồ thị (chỉ dùng cho đồ thị có hướng)

    def themCanh(self, u, v):
        # Thêm cạnh từ u đến v
        self.dinh[u].append(v)
        self.cung += 1  # Tăng số cung khi thêm cạnh

    def SoCungRa(self, v):
        # Trả về số cung đi ra từ đỉnh v
        return len(self.dinh[v])

# Khởi tạo đồ thị và thêm các cạnh
dt = DoThi()
dt.themCanh(1, 2)
dt.themCanh(2, 3)
dt.themCanh(3, 1)
dt.themCanh(2, 4)
dt.themCanh(4, 1)

# Tính số cung đi ra từ đỉnh 2 và in kết quả
socung_ra = dt.SoCungRa(2)
print("Số cung đi ra từ đỉnh 2 là:", socung_ra)
