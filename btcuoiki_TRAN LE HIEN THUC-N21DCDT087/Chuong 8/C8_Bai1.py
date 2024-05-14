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

    def TraTu(self, tu):
        # Hàm băm để lấy ký tự đầu tiên của từ làm key
        key = tu[0].lower()

        # Kiểm tra xem từ có trong từ điển không
        if key in self.tudien:
            return self.tudien[key]['tudongnghia'], self.tudien[key]['tutrainghiem']
        else:
            return [], []  # Trả về list rỗng nếu từ không có trong từ điển


# Sử dụng lớp TuDien để nhập từ và tra từ
td = TuDien()
td.NhapTu("apple", "quả táo", "không phải quả cam")
td.NhapTu("banana", "quả chuối", "không phải quả dừa")

tu_dongnghia, tu_trainghiem = td.TraTu("apple")
print("Từ đồng nghĩa của 'apple':", tu_dongnghia)
print("Từ trái nghĩa của 'apple':", tu_trainghiem)

tu_dongnghia, tu_trainghiem = td.TraTu("banana")
print("Từ đồng nghĩa của 'banana':", tu_dongnghia)
print("Từ trái nghĩa của 'banana':", tu_trainghiem)

tu_dongnghia, tu_trainghiem = td.TraTu("orange")  # Kiểm tra từ không có trong từ điển
print("Từ đồng nghĩa của 'orange':", tu_dongnghia)
print("Từ trái nghĩa của 'orange':", tu_trainghiem)
