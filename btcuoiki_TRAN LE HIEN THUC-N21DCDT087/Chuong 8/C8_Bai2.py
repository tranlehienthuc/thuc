class TuDien:
    def __init__(self):
        self.tudien = {}  # Từ điển chứa các từ, mỗi từ có thể có nhiều đồng nghĩa và trái nghĩa

    def NhapTu(self, tu, dongnghia=None, traita=None):
        # Hàm băm để lấy ký tự đầu tiên của từ làm key
        key = tu[0].lower()

        # Nếu từ chưa có trong từ điển, tạo một entry mới
        if key not in self.tudien:
            self.tudien[key] = {'tudongnghia': [], 'tutrainghiem': []}

        # Thêm từ đồng nghĩa và từ trái nghĩa vào entry tương ứng
        if dongnghia:
            self.tudien[key]['tudongnghia'].append(dongnghia)
        if traita:
            self.tudien[key]['tutrainghiem'].append(traita)

    def DongNghia(self, tu):
        # Hàm băm để lấy ký tự đầu tiên của từ làm key
        key = tu[0].lower()

        # Kiểm tra xem từ có trong từ điển không
        if key in self.tudien:
            return self.tudien[key]['tudongnghia']
        else:
            return []  # Trả về list rỗng nếu từ không có trong từ điển

    def TraiNghia(self, tu):
        # Hàm băm để lấy ký tự đầu tiên của từ làm key
        key = tu[0].lower()

        # Kiểm tra xem từ có trong từ điển không
        if key in self.tudien:
            return self.tudien[key]['tutrainghiem']
        else:
            return []  # Trả về list rỗng nếu từ không có trong từ điển


# Sử dụng lớp TuDien để nhập từ và tra từ
td = TuDien()
td.NhapTu("thông minh", "khôn ngoan", "ngu ngốc")
td.NhapTu("tài năng", "giỏi", "kém")
td.NhapTu("tốt", "tốt lắm", "xấu")

tu_dongnghia = td.DongNghia("thông minh")
tu_traininghia = td.TraiNghia("thông minh")
print("Từ đồng nghĩa của 'thông minh':", tu_dongnghia)
print("Từ trái nghĩa của 'thông minh':", tu_traininghia)

tu_dongnghia = td.DongNghia("tài năng")
tu_traininghia = td.TraiNghia("tài năng")
print("Từ đồng nghĩa của 'tài năng':", tu_dongnghia)
print("Từ trái nghĩa của 'tài năng':", tu_traininghia)

tu_dongnghia = td.DongNghia("không")
tu_traininghia = td.TraiNghia("không")
print("Từ đồng nghĩa của 'không':", tu_dongnghia)
print("Từ trái nghĩa của 'không':", tu_traininghia)
