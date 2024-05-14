def Cong(a, b):
    result = []
    c = 0
    len_a = len(a)
    len_b = len(b)
    max_len = max(len_a, len_b)

    for i in range(1, max_len + 1):
        digit_a = int(a[-i]) if i <= len_a else 0
        digit_b = int(b[-i]) if i <= len_b else 0
        total = digit_a + digit_b + c

        if total > 9:
            result.append(-1)
            c = 1
        else:
            result.append(total)
            c = 0
    if c == 1:
        result.append(1)
    return result[::-1]
a = [1, 2, 3] 
b = [9, 8, 7]  
print("Kết quả của a + b là:", Cong(a, b))
