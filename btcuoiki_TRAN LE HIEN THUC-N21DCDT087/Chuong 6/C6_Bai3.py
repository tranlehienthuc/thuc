def Giao(a, b):
    # Sắp xếp mảng a và b để dễ dàng so sánh và thực hiện phép giao
    a.sort()
    b.sort()

    # Khởi tạo mảng c để chứa kết quả
    c = []
    # Duyệt qua từng phần tử trong mảng a
    for num in a:
        # Kiểm tra xem phần tử num có trong cả mảng a và b không
        if num in b and num not in c:
            c.append(num)  # Nếu có, thêm vào mảng c

    return c
# Mảng a và b ban đầu
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
# Gọi phương thức Giao và in kết quả
c = Giao(a, b)
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng c (Giao):", c)
