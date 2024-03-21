def factorial(n): #khai báo hàm giai thừa với biến n
    if n == 0: #nếu n bằng 0 sẽ trả về 1
        return 1
    else:
        return n * factorial(n-1)
def Neper(n):
    if n < 0:
        return "n phải lớn hơn hoặc bằng 0"
    e_sum = 0
    for k in range(n + 1):
        e_sum += 1 / factorial(k)
    return e_sum

#Ví dụ n = 9
n = 9
print("Tổng của các số hạng", n, "là:", Neper(n))