def Hop(a, b):
    # Sắp xếp mảng a và b để dễ dàng thực hiện phép hợp và loại bỏ các phần tử trùng nhau
    a.sort()
    b.sort()

    # Khởi tạo mảng c để chứa kết quả
    c = []

    # Duyệt qua từng phần tử trong mảng a
    for num in a:
        if num not in c:  # Kiểm tra xem phần tử num đã có trong mảng c chưa
            c.append(num)  # Nếu chưa có, thêm vào mảng c

    # Duyệt qua từng phần tử trong mảng b
    for num in b:
        if num not in c:  # Kiểm tra xem phần tử num đã có trong mảng c chưa
            c.append(num)  # Nếu chưa có, thêm vào mảng c

    c.sort()  # Sắp xếp mảng c tăng dần

    return c
# Mảng a và b ban đầu
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

# Gọi phương thức Hop và in kết quả
c = Hop(a, b)
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng c (Hợp):", c)
