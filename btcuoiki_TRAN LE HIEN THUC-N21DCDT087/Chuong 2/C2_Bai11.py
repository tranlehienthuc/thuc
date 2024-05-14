def Cong(sign_a, digits_a, sign_b, digits_b):
    def array_to_int(sign, digits):
        num = int(''.join(map(str, digits)))
        return -num if sign else num
    def is_overflow(num):
        return num > 2147483647 or num < -2147483648
    num_a = array_to_int(sign_a, digits_a)
    num_b = array_to_int(sign_b, digits_b)
    result = num_a + num_b
    if is_overflow(result):
        return [-1]
    sign_result = 0 if result >= 0 else 1
    digits_result = [int(digit) for digit in str(abs(result))]
    return sign_result, digits_result
sign_a, digits_a = 0, [1, 2, 3]  
sign_b, digits_b = 1, [4, 5]     
result = Cong(sign_a, digits_a, sign_b, digits_b)
print(f"Kết quả: {result}")