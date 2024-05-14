from collections import defaultdict

class DoThi:
    def __init__(self):
        self.dinh = defaultdict(list)  # Danh sách kề của mỗi đỉnh trong đồ thị

    def themCanh(self, u, v):
        # Thêm cạnh từ u đến v
        self.dinh[u].append(v)
        # Thêm cạnh từ v đến u (nếu là đồ thị vô hướng)
        self.dinh[v].append(u)

    def DFS(self, u, visited, parent):
        # Đánh dấu đỉnh u là đã được thăm
        visited[u] = True

        # Duyệt qua tất cả các đỉnh kề với u
        for v in self.dinh[u]:
            # Nếu đỉnh v chưa được thăm, tiến hành duyệt DFS từ v
            if not visited[v]:
                if self.DFS(v, visited, u):  # Nếu tìm thấy chu trình trong DFS
                    return True
            # Nếu đỉnh v đã được thăm và không phải là cha của u, tức là tìm thấy chu trình
            elif parent != v:
                return True

        return False

    def ChuTrinh(self):
        # Khởi tạo danh sách đánh dấu cho các đỉnh
        visited = {v: False for v in self.dinh}

        # Duyệt qua tất cả các đỉnh và thực hiện DFS từ các đỉnh chưa được thăm
        for v in visited:
            if not visited[v]:
                if self.DFS(v, visited, None):  # Nếu tìm thấy chu trình trong DFS
                    return True

        return False
# Khởi tạo đồ thị và thêm các cạnh
dt = DoThi()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
# Kiểm tra xem đồ thị có chứa chu trình hay không và in kết quả
if dt.ChuTrinh():
    print("Đồ thị có chu trình.")
else:
    print("Đồ thị không có chu trình.")
