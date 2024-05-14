from collections import defaultdict

class DoThi:
    def __init__(self):
        self.dinh = defaultdict(list)  # Danh sách kề của mỗi đỉnh trong đồ thị

    def themCanh(self, u, v):
        # Thêm cạnh từ u đến v
        self.dinh[u].append(v)
        # Thêm cạnh từ v đến u (nếu là đồ thị vô hướng)
        self.dinh[v].append(u)

    def DFS(self, u, visited, v2):
        # Đánh dấu đỉnh u là đã được thăm
        visited[u] = True

        # Nếu đỉnh u là đỉnh đích v2, trả về True
        if u == v2:
            return True

        # Duyệt qua tất cả các đỉnh kề với u
        for v in self.dinh[u]:
            if not visited[v]:
                if self.DFS(v, visited, v2):  # Nếu tìm thấy đường đi từ v đến v2
                    return True

        return False

    def DuongDi(self, v1, v2):
        # Khởi tạo danh sách đánh dấu cho các đỉnh
        visited = {v: False for v in self.dinh}

        # Gọi hàm DFS để kiểm tra xem có đường đi từ v1 đến v2 không
        return self.DFS(v1, visited, v2)

# Khởi tạo đồ thị và thêm các cạnh
dt = DoThi()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(2, 3)

# Kiểm tra xem có đường đi từ đỉnh 0 đến đỉnh 3 không và in kết quả
if dt.DuongDi(0, 3):
    print("Có đường đi từ đỉnh 0 đến đỉnh 3.")
else:
    print("Không có đường đi từ đỉnh 0 đến đỉnh 3.")
