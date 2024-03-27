def Tru(a, b):
    result = []
    c = 0
    len_a = len(a)
    len_b = len(b)
    max_len = len_a
    for i in range(1, max_len + 1):
        digit_a = int(a[-i])
        digit_b = int(b[-i]) if i <= len_b else 0
        diff = digit_a - digit_b - c
        if diff < 0:
            diff += 10
            c = 1
        else:
            c = 0
        result.append(diff)
    while result[-1] == 0 and len(result) > 1:
        result.pop()
    return result[::-1]
a = [7, 8, 9, 2]  
b = [3, 2, 5]     
print("Kết quả của a - b là:", Tru(a, b))
