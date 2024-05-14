from collections import defaultdict

class DoThi:
    def __init__(self):
        self.dinh = defaultdict(list)  # Danh sách kề của mỗi đỉnh trong đồ thị

    def themCanh(self, u, v):
        # Thêm cạnh từ u đến v
        self.dinh[u].append(v)
        # Thêm cạnh từ v đến u (nếu là đồ thị vô hướng)
        self.dinh[v].append(u)

    def DFS(self, u, visited):
        # Đánh dấu đỉnh u là đã được thăm
        visited[u] = True

        # Duyệt qua tất cả các đỉnh kề với u
        for v in self.dinh[u]:
            if not visited[v]:
                self.DFS(v, visited)

    def SoThanhPhan(self):
        # Khởi tạo danh sách đánh dấu cho các đỉnh
        visited = {v: False for v in self.dinh}

        # Khởi tạo biến đếm số thành phần liên thông
        count = 0

        # Duyệt qua tất cả các đỉnh và thực hiện DFS từ các đỉnh chưa được thăm
        for v in visited:
            if not visited[v]:
                self.DFS(v, visited)
                count += 1

        return count

# Khởi tạo đồ thị và thêm các cạnh
dt = DoThi()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(3, 4)

# In số thành phần liên thông của đồ thị
print("Số thành phần liên thông của đồ thị:", dt.SoThanhPhan())
