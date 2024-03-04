def tuple_elementwise_sum(tuple1, tuple2):
    output_tuple = tuple(x + y for x, y in zip(tuple1, tuple2))
    # Trả về tuple chứa kết quả
    return output_tuple
# Sử dụng ví dụ
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# In tuple chứa tổng từng phần tử tương ứng
print(output_tuple)
