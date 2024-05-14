def fibonacci(n): #khai báo hàm giai thừa với biến n
    if n == 0: #nếu n bằng 0 sẽ trả về 0
        return 0
    elif n == 1: #nếu n bằng 1 sẽ trả về 1
        return 1
    else:# ngược lại sẽ bằng fibonacci(n - 1) + fibonacci(n - 2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ví dụ
n = 7
result = fibonacci(n)
print(f"Số Fibonacci thứ {n} là: {result}")