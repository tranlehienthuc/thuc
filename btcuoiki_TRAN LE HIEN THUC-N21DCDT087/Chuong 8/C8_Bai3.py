# Định nghĩa lớp BaiHat để lưu thông tin của một bài hát
class BaiHat:
    def __init__(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
        self.ten_bai_hat = ten_bai_hat  # Tên của bài hát
        self.ten_nhac_si = ten_nhac_si  # Tên của nhạc sĩ sáng tác bài hát
        self.ten_ca_si = ten_ca_si      # Tên của ca sĩ biểu diễn bài hát

# Định nghĩa lớp Album để lưu thông tin của một album
class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album    # Tên của album
        self.bai_hat_list = []        # Danh sách các bài hát trong album

# Định nghĩa lớp TuDien để quản lý và xử lý thông tin các album
class TuDien:
    def __init__(self):
        self.danh_sach_album = {}  # Từ điển các album, key là tên album và value là đối tượng Album

    # Phương thức để nhập thông tin của một album và các bài hát trong album
    def NhapAlbum(self):
        ten_album = input("Nhập tên album: ")  # Nhập tên album từ người dùng
        album = Album(ten_album)               # Tạo một đối tượng Album mới
        so_bai_hat = int(input("Nhập số bài hát trong album: "))  # Nhập số lượng bài hát trong album
        for i in range(so_bai_hat):
            ten_bai_hat = input(f"Nhập tên bài hát {i+1}: ")        # Nhập tên của mỗi bài hát
            ten_nhac_si = input(f"Nhập tên nhạc sĩ của bài hát {ten_bai_hat}: ")  # Nhập tên nhạc sĩ của bài hát
            ten_ca_si = input(f"Nhập tên ca sĩ của bài hát {ten_bai_hat}: ")      # Nhập tên ca sĩ biểu diễn bài hát
            bai_hat = BaiHat(ten_bai_hat, ten_nhac_si, ten_ca_si)  # Tạo một đối tượng BaiHat mới
            album.bai_hat_list.append(bai_hat)  # Thêm bài hát vào danh sách bài hát của album
        self.danh_sach_album[ten_album] = album  # Thêm album vào từ điển các album

    # Phương thức để xem thông tin của một album dựa trên tên album
    def XemAlbum(self, ten):
        if ten in self.danh_sach_album:  # Kiểm tra xem album có tồn tại trong từ điển không
            album = self.danh_sach_album[ten]  # Lấy đối tượng Album tương ứng với tên album
            print(f"Thông tin album {album.ten_album}:")
            for i, bai_hat in enumerate(album.bai_hat_list, 1):
                print(f"Bài hát {i}: {bai_hat.ten_bai_hat}")
                print(f"   - Nhạc sĩ: {bai_hat.ten_nhac_si}")
                print(f"   - Ca sĩ: {bai_hat.ten_ca_si}")
        else:
            print("Không tìm thấy album này trong từ điển.")

# Tạo một đối tượng TuDien để sử dụng
tudien = TuDien()

# Nhập thông tin của một album
tudien.NhapAlbum()

# Xem thông tin của một album
ten_can_tim = input("Nhập tên album cần xem: ")
tudien.XemAlbum(ten_can_tim)
