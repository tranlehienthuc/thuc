def common_elements(num_list1, num_list2):
    # Chuyển đổi danh sách thành tập hợp để loại bỏ các phần tử trùng lặp
    set1 = set(num_list1)
    set2 = set(num_list2)
    # Sử dụng phép giao của hai tập hợp để tìm các phần tử chung
    common_nums = set1.intersection(set2)

    # Chuyển đổi kết quả từ tập hợp thành danh sách
    return list(common_nums)
# Kiểm tra với input đã cung cấp
num_list1 = [1, 2, 3, 4, 5]
num_list2 = [4, 5, 6, 7, 8]
print(common_elements(num_list1, num_list2))  # Output: [4, 5]
