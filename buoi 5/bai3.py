def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Tạo một bản sao của từ điển thứ nhất để tránh sửa đổi trực tiếp
    merged_dict.update(dict2)  # Cập nhật bản sao với từ điển thứ hai
    return merged_dict
# Sử dụng ví dụ
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
result_dict = merge_dicts(dict1, dict2)
print(result_dict)
