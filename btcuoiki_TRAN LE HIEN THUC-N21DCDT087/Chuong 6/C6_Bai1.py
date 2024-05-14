def Duynhat(a):
    # Sắp xếp mảng a để dễ dàng loại bỏ các phần tử trùng nhau
    a.sort()
    unique_list = []
    # Duyệt qua mảng a để thêm các phần tử duy nhất vào unique_list
    for i in range(len(a)):
        # Nếu phần tử hiện tại không trùng với phần tử trước đó
        if i == 0 or a[i] != a[i - 1]:
            unique_list.append(a[i])
    return unique_list

# Test với một mảng a
a = [1, 5, 3, 7, 5, 9, 7]
b = Duynhat(a)
print("Mảng a:", a)
print("Mảng b:", b)
