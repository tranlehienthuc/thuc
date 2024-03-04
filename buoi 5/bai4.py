def filter_dict(input_dict, condition):
    # Tạo một từ điển mới để lưu trữ kết quả lọc
    filtered_dict = {}
    # Duyệt qua từng cặp key-value trong từ điển đầu vào
    for key, value in input_dict.items():
        # Kiểm tra xem cặp key-value hiện tại thỏa mãn điều kiện hay không
        if condition(key, value):
            # Nếu thỏa mãn, thêm cặp key-value vào từ điển mới
            filtered_dict[key] = value
    # Trả về từ điển mới sau khi lọc
    return filtered_dict
# Sử dụng hàm filter_dict
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Sử dụng lambda function để kiểm tra xem giá trị có phải là số chẵn không
filter_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
# In kết quả lọc ra màn hình
print(filter_dict)
