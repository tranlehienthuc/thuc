from collections import defaultdict
#
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

    def LienThong(self):
        # Khởi tạo danh sách đánh dấu cho các đỉnh
        visited = {v: False for v in self.dinh}

        # Chọn một đỉnh bất kỳ để bắt đầu DFS
        start_vertex = next(iter(self.dinh))

        # Thực hiện DFS từ đỉnh start_vertex
        self.DFS(start_vertex, visited)

        # Kiểm tra xem tất cả các đỉnh đã được thăm chưa
        return all(visited.values())

# Khởi tạo đồ thị và thêm các cạnh
dt = DoThi()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(3, 4)

# Kiểm tra đồ thị liên thông và in kết quả
if dt.LienThong():
    print("Đồ thị là đồ thị liên thông.")
else:
    print("Đồ thị không là đồ thị liên thông.")
