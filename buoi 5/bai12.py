def concatenate_strings(input_tuple):
    output_string = ''.join(input_tuple)
    return output_string
# Sử dụng hàm concatenate_strings
input_tuple = ("hello", "world", ' from', ' Python')
output_string = concatenate_strings(input_tuple)
# In kết quả ra màn hình
print(output_string)
