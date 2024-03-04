def sum_product(input_tuple):
    # Tính tổng các phần tử trong tuple
    sum_result = sum(input_tuple)
    # Tính tích các phần tử trong tuple
    product_result = 1
    for num in input_tuple:
        product_result *= num
    # Tính kết quả bằng cách nhân sum_result và product_result
    result = sum_result * product_result
    # Trả về các giá trị đã tính
    return sum_result, product_result, result
# Sử dụng ví dụ
input_tuple = (1, 2, 3, 4)
sum_result, product_result, result = sum_product(input_tuple)
# In tổng và tích
print("Tổng:", sum_result)
print("Tích:", product_result)
