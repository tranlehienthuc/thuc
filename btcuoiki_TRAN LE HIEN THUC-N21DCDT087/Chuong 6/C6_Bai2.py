def Hieu(a, b):
    # Sắp xếp mảng a và b để dễ dàng so sánh và thực hiện phép hiệu
    a.sort()
    b.sort()
    # Khởi tạo mảng c để chứa kết quả
    c = []
    # Duyệt qua từng phần tử trong mảng a
    for num in a:
        # Kiểm tra xem phần tử num có trong mảng b không
        if num not in b:
            c.append(num)  # Nếu không có, thêm vào mảng c
    return c
# Mảng a và b ban đầu
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
# Gọi phương thức Hieu và in kết quả
c = Hieu(a, b)
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng c:", c)
