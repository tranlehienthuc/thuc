def max_in_sliding_window(num_list, size):
    if not num_list:
        return []
    result = []
    window = []  # List de luu tru cac chi muc cua cac so trong cua so
    # Duyet qua tung so trong danh sach
    for i, num in enumerate(num_list):
        # Loai bo cac chi muc khoi cua so vuot qua kich thuoc cua so
        while window and window[0] <= i - size:
            window.pop(0)
        # Loai bo cac phan tu nho hon phan tu moi them vao tu phia sau cua so
        while window and num_list[window[-1]] < num:
            window.pop()
        # Them muc cua phan tu vao cua so
        window.append(i)
        # Neu cua so da du kich thuoc, them so lon nhat vao ket qua
        if i >= size - 1:
            result.append(num_list[window[0]])

    return result
# Kiem tra voi input da cung cap
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
size = 3
print(max_in_sliding_window(num_list, size))  # Output: [5, 5, 5, 5, 10, 12, 33, 33]
