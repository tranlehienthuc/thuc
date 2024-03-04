def insert_value_front(input_tuple, value_to_insert):
    # Chuyển đổi tuple thành list để có thể thay đổi nội dung
    list_version = list(input_tuple)
    # Chèn giá trị vào đầu list
    list_version.insert(0, value_to_insert)
    # Chuyển lại list thành tuple
    output_tuple = tuple(list_version)
    return output_tuple
# Sử dụng hàm insert_value_front
input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
# In kết quả ra màn hình
print(output_tuple)
