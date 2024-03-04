def check_same_frequency(list1, list2):
    # Tạo từ điển để lưu trữ tần suất xuất hiện của phần tử trong list1
    frequency_dict = {}
    # Duyệt qua list1 và cập nhật tần suất xuất hiện trong frequency_dict
    for item in list1:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    # Duyệt qua list2 và kiểm tra tần suất xuất hiện trong frequency_dict
    for item in list2:
        # Nếu phần tử không có trong frequency_dict hoặc tần suất xuất hiện không giống nhau, trả về False
        if item not in frequency_dict or frequency_dict[item] == 0:
            return False
        # Giảm tần suất xuất hiện trong frequency_dict
        frequency_dict[item] = 1
    # Kiểm tra xem tất cả các phần tử đã được kiểm tra hay chưa
    return all(frequency == 0 for frequency in frequency_dict.values())
# Sử dụng hàm check_same_frequency
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
result = check_same_frequency(list1, list2)

# In kết quả ra màn hình
print(result)
